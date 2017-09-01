# -*- coding: utf-8 -*-
import numpy as np
from random import randint
import os
import json
import settings
import cPickle
import nltk.data
from pyvi.pyvi import ViTokenizer
from sklearn.svm import LinearSVC
from gensim import corpora, matutils
from sklearn.metrics import classification_report

class FileReader(object):
    def __init__(self, filePath, encoder = None):
        self.filePath = filePath
        self.encoder = encoder if encoder != None else 'utf-16le'

    def read(self):
        with open(self.filePath) as f:
            s = f.read()
        return s

    def content(self):
        s = self.read()
        return s.decode(self.encoder)

    def read_json(self):
        with open(self.filePath) as f:
            s = json.load(f)
        return s

    def read_stopwords(self):
        with open(self.filePath, 'r') as f:
            stopwords = set([w.strip().replace(' ', '_') for w in f.readlines()])
        return stopwords

    def load_dictionary(self):
        return corpora.Dictionary.load_from_text(self.filePath)

class FileStore(object):
    def __init__(self, filePath, data = None):
        self.filePath = filePath
        self.data = data

    def store_json(self):
        with open(self.filePath, 'w') as outfile:
            json.dump(self.data, outfile)

    def store_dictionary(self, dict_words):
        dictionary = corpora.Dictionary(dict_words)
        dictionary.filter_extremes(no_below=20, no_above=0.3)
        dictionary.save_as_text(self.filePath)

    def save_pickle(self,  obj):
        outfile = open(self.filePath, 'wb')
        fastPickler = cPickle.Pickler(outfile, cPickle.HIGHEST_PROTOCOL)
        fastPickler.fast = 1
        fastPickler.dump(obj)
        outfile.close()

class DataLoader(object):
    def __init__(self, dataPath):
        self.dataPath = dataPath

    def __get_files(self):
        folders = [self.dataPath + folder + '/' for folder in os.listdir(self.dataPath)]
        class_titles = os.listdir(self.dataPath)
        files = {}
        for folder, title in zip(folders, class_titles):
            files[title] = [folder + f for f in os.listdir(folder)]
        self.files = files

    def get_json(self):
        self.__get_files()
        data = []
        for topic in self.files:
            rand = randint(100, 150)
            i = 0
            for file in self.files[topic]:
                content = FileReader(filePath=file).content()
                data.append({
                    'category': topic,
                    'content': content
                })
                if i == rand:
                    break
                else:
                    i += 1
        return data

class NLP(object):
    def __init__(self, text = None):
        self.text = text
        self.__set_stopwords()

    def __set_stopwords(self):
        self.stopwords = FileReader(settings.STOP_WORDS).read_stopwords()

    def segmentation(self):
        return ViTokenizer.tokenize(self.text)

    def split_words(self):
        text = self.segmentation()
        try:
            return [x.strip(settings.SPECIAL_CHARACTER).lower() for x in text.split()]
        except TypeError:
            return []

    def get_words_feature(self):
        split_words = self.split_words()
        return [word for word in split_words if word.encode('utf-8') not in self.stopwords]

class FeatureExtraction(object):
    def __init__(self, data):
        self.data = data

    def __build_dictionary(self):
        print 'Building dictionary'
        dict_words = []
        i = 0
        for text in self.data:
            i += 1
            print "Step {} / {}".format(i, len(self.data))
            words = NLP(text = text['content']).get_words_feature()
            dict_words.append(words)
        FileStore(filePath=settings.DICTIONARY_PATH).store_dictionary(dict_words)

    def __load_dictionary(self):
        if os.path.exists(settings.DICTIONARY_PATH) == False:
            self.__build_dictionary()
        self.dictionary = FileReader(settings.DICTIONARY_PATH).load_dictionary()

    def __build_dataset(self):
        self.features = []
        self.labels = []
        i = 0
        for d in self.data:
            i += 1
            print "Step {} / {}".format(i, len(self.data))
            self.features.append(self.get_dense(d['content']))
            self.labels.append(d['category'])

    def get_dense(self, text):
        self.__load_dictionary()
        words = NLP(text).get_words_feature()
        # Bag of words
        vec = self.dictionary.doc2bow(words)
        dense = list(matutils.corpus2dense([vec], num_terms=len(self.dictionary)).T[0])
        return dense

    def get_data_and_label(self):
        self.__build_dataset()
        return self.features, self.labels

class Classifier(object):
    def __init__(self, features_train = None, labels_train = None, features_test = None, labels_test = None,  estimator = LinearSVC(random_state=0)):
        self.features_train = features_train
        self.features_test = features_test
        self.labels_train = labels_train
        self.labels_test = labels_test
        self.estimator = estimator

    def training(self):
        self.estimator.fit(self.features_train, self.labels_train)
        self.__training_result()

    def save_model(self, filePath):
        FileStore(filePath=filePath).save_pickle(obj=est)

    def __training_result(self):
        y_true, y_pred = self.labels_test, self.estimator.predict(self.features_test)
        print(classification_report(y_true, y_pred))

if __name__ == '__main__':
    json_train = DataLoader(dataPath=settings.DATA_TRAIN_PATH).get_json()
    FileStore(filePath=settings.DATA_TRAIN_JSON, data=json_train).store_json()
    json_test = DataLoader(dataPath=settings.DATA_TEST_PATH).get_json()
    FileStore(filePath=settings.DATA_TEST_JSON, data=json_test).store_json()
    train_loader = FileReader(filePath=settings.DATA_TRAIN_JSON)
    test_loader = FileReader(filePath=settings.DATA_TEST_JSON)
    data_train = train_loader.read_json()
    data_test = test_loader.read_json()

    features_train, labels_train = FeatureExtraction(data=data_train).get_data_and_label()
    features_test, labels_test = FeatureExtraction(data=data_test).get_data_and_label()

    est = Classifier(features_train=features_train, features_test=features_test, labels_train=labels_train, labels_test=labels_test)
    est.training()
    est.save_model(filePath='trained_model/linear_svc_model.pk')