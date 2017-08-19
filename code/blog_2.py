from sklearn.metrics import classification_report
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm


def evaluate_model(X_test, y_test):
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))

if __name__ == "__main__":
    # Load data
    iris = load_iris()

    # Print data
    print "Size of data", iris.data.shape
    print "Target", iris.target

    # Tach tap du lieu
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

    # Training SVC
    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)

    # Evaluate SVC
    print "SVC result"
    evaluate_model(X_test, y_test)

    # Training Random Forest
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Evaluate Random Forest
    print "Random Forest result"
    evaluate_model(X_test, y_test)

    # Training Naive Bayes
    clf = GaussianNB()
    clf.fit(X_train, y_train)

    # Evaluate Naive Bayes
    print "Random Forest result"
    evaluate_model(X_test, y_test)