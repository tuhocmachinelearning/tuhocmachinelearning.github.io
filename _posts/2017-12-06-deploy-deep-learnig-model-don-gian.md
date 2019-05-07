---
title: "Blog #11 - Deploy mô hình Deep Learning lên production một cách đơn giản"
last_modified_at: 2017-10-06T16:20:02-05:00
categories:
  - Deployment
tags:
  - Deployment
teaser: 'http://debugmycode.com/wp-content/uploads/2017/05/Nasuni_cover_pic.jpg'

excerpt: 'Deep Learning là một thứ rất hay ho nhưng nó không hề dễ tiếp cận với người mới bắt đầu. Việc training Deep Learning làm sao để ra được một mô hình tốt thực sự là một thử thách lớn đối khá nhiều người. Tuy nhiên giả sử như khi bạn đã có một mô hình tốt thì cũng không phải dễ dàng cho người mới bắt đầu vì kiến trúc server của nó khá khác lạ so với các kiến trúc Web Services thông thường. Nếu bạn đang vướng mắc trong vấn đề deploy mô hình Deep Learning trên server thì bài viết này chính là câu trả lời dành cho bạn.'

sidebar:
  nav: "docs"

---
{% include toc %}

Deep Learning là một thứ rất hay ho nhưng nó không hề dễ tiếp cận với người mới bắt đầu. Việc training Deep Learning làm sao để ra được một mô hình tốt thực sự là một thử thách lớn đối khá nhiều người. Tuy nhiên giả sử như khi bạn đã có một mô hình tốt thì cũng không phải dễ dàng cho người mới bắt đầu vì kiến trúc server của nó khá khác lạ so với các kiến trúc Web Services thông thường. Nếu bạn đang vướng mắc trong vấn đề deploy mô hình Deep Learning trên server thì bài viết này chính là câu trả lời dành cho bạn.

# Sử dụng các hệ thống Cloud 

Điều đầu tiên bạn có thê nghĩ ngay đến đó chính là việc sử dụng các hệ thống cloud từ bên thứ ba. Hãy thử một vài hệ thống của các ông lớn về công nghệ như Google, Facebook, Microsoft, Amazon... Họ đều cung cấp các giải pháp cho phép bạn có thể triển khai các mô hình chạy Deep Learning với một chi phí có thể chấp nhận được. 

![](http://debugmycode.com/wp-content/uploads/2017/05/Nasuni_cover_pic.jpg)

Tuy nhiên nếu như bạn muốn tự mình triển khai một hệ thống server có thể chạy được các mô hình Deep Learning thì sao. Điều này cũng là một việc nên làm vì sử dụng Cloud của bên thứ ba cũng có một vài điểm hạn chế như sau:

* Sử dụng hệ thống của bên thứ ba có nghĩa là bạn chấp nhận rằng mình hoàn toàn bị động về vấn đề kiến trúc hệ thống và điều đó rất khó khăn cho vấn đề maintain - bảo trì sau này. Khi có vấn đề nào đó xảy ra bạn lại phải mất công chờ đợi đội ngũ support từ bên thứ ba và điều này thường là không mấy thoải mái chút nào.
* Chi phí cho các hệ thống này thường không phải là rẻ. Nếu như tự triển khai kiến trúc riêng của mình bạn chỉ phải tốn tiền đầu tư một lần thì sử dụng Cloud của bên thứ ba bạn cũng hoàn toàn bị động về các chi phí phát sinh (thường là theo số lượng request).

Chính vì lý do đó mình sẽ hướng dẫn các bạn triển khai một kiến trúc server đủ đơn giản để dễ dàng cho việc deploy nhưng cũng đủ mạnh mẽ để đáp ứng được yêu cầu của bạn khi chạy một ứng dụng Deep Learning. OK chúng ta bắt đầu thôi 



# Kiến trúc hệ thống 

Có rất nhiều ngôn ngữ hỗ trợ chúng ta việc cài đặt các thuật toán Deep Learning nhưng có lẽ phổ biến hơn cả đó chính là Python. Hầu như khi nghĩ đến AI người ta nghĩ ngay đến Python. Trong bài viết này mình cũng chia sẻ với các bạn chính bằng ngôn ngữ này nên nếu bạn nào chưa có nhiều kinh nghiệm làm việc với Python thì hãy cố gắng tìm kiếm lại các bài viết khác trên **Viblo** nhé. Chúng ta sẽ cùng xây dựng hệ thống của mình thông qua các thư viện đơn giản nhất bằng ngôn ngữ Python sau đây:

* **Keras** dùng trong việc training các giải thuật Deep Learning
* **Flask** là một framework rất đơn giản để dùng để viết Web Service bằng ngôn ngữ Python 
* **Redis** sử dụng để caching mô hình Deep Learning trên môi trường production 

Vậy là các thành phần cần thiết để xây dựng hệ thống chúng ta đã hoàn thành. Giờ chúng ta sẽ đi vào chi tiết hơn nhé 

## Cài đặt môi trường 

### Cài đặt và cấu hình Redis 

**Redis** là một công cụ khá phổ biến và bạn có thể dễ dàng cài đặt nó trong phần sau:

```
$ wget http://download.redis.io/redis-stable.tar.gz
$ tar xvzf redis-stable.tar.gz
$ cd redis-stable
$ make
$ sudo make install
```

Để khởi động **Redis** chúng ta có thể sử dụng câu lệnh sau 

```
$ redis-server
```
Các bạn có thể sử dụng câu lệnh sau để test sự hoạt động của **Redis**:

```
$ redis-cli ping
PONG
```

Nếu kết quả hiện chữ **PONG** thì có nghĩa là ok.

### Cấu hình virtualenv để chạy ứng dụng 

Các bạn sử dụng các thư viện sau trong suốt quá trình thực hiện Project này. Theo mình thì các bạn nên tạo một [virtualenv](https://virtualenv.pypa.io/en/stable/) để cài đặt các package cần thiết sau:

```python
$ pip install numpy
$ pip install scipy h5py
$ pip install tensorflow # tensorflow-gpu for GPU machines
$ pip install keras
$ pip install flask gevent
$ pip install imutils requests
$ pip install redis
$ pip install Pillow
```

Trong ứng dụng demo về nhận diện ảnh nhưng chúng ta không cần sử dụng thư viện **OpenCV** mà chỉ cần sử dụng **PIL** thay cho nó vì chủ yếu chúng ta xử lý ảnh dựa trên kiểu Bytes tức là truyền lên sử dụng Base64 mà thư viện PIL xử lý rất tốt vấn đề này. Sau đây chúng ta sẽ cùng bàn về luồng xử lý ứng dụng REST API cho Deep Learning nhé 

### Luồng xử lý 

![](https://www.pyimagesearch.com/wp-content/uploads/2018/01/keras_api_data_flow.png)

Như chúng ta thấy ở trên sơ đồ trên thì sau khi ảnh được gửi lên thông qua REST API sẽ được xử lý và convert về dạng Base64 (bạn cũng có thể convert thành Base64 dưới Client rồi truyền lên theo REST API tuỳ vào mục đích xử lý của bạn) thông qua Flask sau đó sẽ được đẩy vào Queue của Redis. Redis thực hiện xử lý predict model thông qua cấu hình model đã được load lúc khởi chạy server. Sau đó kết quả dự đoán lại được trả về thông qua Queue. Flask chỉ việc lấy thông tin dự đoán từ queue và trả về cho client thông qua response đồng thời xoá dữ liệu ra khỏi queue này.  Điểm mấu chốt của nó chính là việc sử dụng **Redis** để caching lại mô hình học máy điều này làm tăng hiệu năng của hệ thống lên rất nhiều. 

## Cấu trúc thư mục Flask 

Sau khi cài đặt Flask các bạn tổ chức các file code theo cấu trúc sau: 

```
├── helpers.py
├── keras_rest_api_app.wsgi
├── run_model_server.py
├── run_web_server.py
├── settings.py
├── simple_request.py
└── stress_test.py
```

Trong đó:

* File ```run_web_server.py```: chứa tất cả code của Flask web server code.
* File ```run_model_server.py```: thực hiện các công việc 
    * Load Keras model dưới dạng file **h5** và **json**
    * Liên tục truy cập vào Redis để lấy thông tin các ảnh gửi tới qua web request và tiến hành phân loại ảnh 
    * Ghi kết quả phân loại vào Redis 

* ```settings.py```: chứa tất cả các cài đặt cần thiết 
* ```keras_rest_api_app.wsgi```: chứa các **WSGI** setting giúp chạy ứng dụng Flask trên môi trường Apache server. 
* ```simple_request.py```: Sử dụng để điều hướng các request thông qua REST API

## Cấu hình file ```settings.py```
Chúng ta cài đặt các thông số cho hệ thống trong file ```settings.py``` như sau:

```python
# initialize Redis connection settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
 
# initialize constants used to control image spatial dimensions and
# data type
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "float32"
 
# initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 32
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25
```

Các bài cài đặt lại thông số sao cho phù hợp với cấu hình Redis trên server của mình là được. Có một vài thông số tuỳ thuộc vào cấu hình của server bạn đang sử dụng như thông số ```BATCH_SIZE = 32``` tức là xử lý 32 ảnh trong một lần predict. Thông số này được sử dụng trên máy có GPU của mình. Các bạn nên cầu hình lại cho phù hợp để tận dụng tối đa hiệu năng của hệ thống, không để thừa thãi và cũng không để cạn kiệt tài nguyên hệ thống. 

## Helpers function 

Chúng ta cài đặt một số hàm xử lý encode và deocde ảnh dưới dạng Base64 trong file ```helpers.py```

```python
# import the necessary packages
import numpy as np
import base64
import sys

def base64_encode_image(a):
  # base64 encode the input NumPy array
  return base64.b64encode(a).decode("utf-8")

def base64_decode_image(a, dtype, shape):
  # if this is Python 3, we need the extra step of encoding the
  # serialized NumPy string as a byte object
  if sys.version_info.major == 3:
    a = bytes(a, encoding="utf-8")

  # convert the string to a NumPy array using the supplied data
  # type and target shape
  a = np.frombuffer(base64.decodestring(a), dtype=dtype)
  a = a.reshape(shape)

  # return the decoded image
  return a
```

Các encode là cần thiết để có thể truyền tải và lưu trữ ảnh thông qua Redis. Việc decode cũng vậy, nó giúp chúng ta thực hiện thao tác tiền xử lý hình ảnh trước khi đưa vào mô hình để dự đoán 

## Web server

Để tiến hành xử lý thông tin gửi lên thông qua REST API chúng ta sử dụng cấu trúc mặc định của Flask. Nhận đầu vào là ảnh và trả về kết quả là JSON. 

```python 
# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import settings
import helpers
import flask
import redis
import uuid
import time
import json
import io

# initialize our Flask application and Redis server
app = flask.Flask(__name__)
db = redis.StrictRedis(host=settings.REDIS_HOST,
  port=settings.REDIS_PORT, db=settings.REDIS_DB)

def prepare_image(image, target):
  # if the image mode is not RGB, convert it
  if image.mode != "RGB":
    image = image.convert("RGB")

  # resize the input image and preprocess it
  image = image.resize(target)
  image = img_to_array(image)
  image = np.expand_dims(image, axis=0)
  image = imagenet_utils.preprocess_input(image)

  # return the processed image
  return image

@app.route("/")
def homepage():
  return "Welcome to the Keras REST API!"

@app.route("/predict", methods=["POST"])
def predict():
  # initialize the data dictionary that will be returned from the
  # view
  data = {"success": False}

  # ensure an image was properly uploaded to our endpoint
  if flask.request.method == "POST":
    if flask.request.files.get("image"):
      # read the image in PIL format and prepare it for
      # classification
      image = flask.request.files["image"].read()
      image = Image.open(io.BytesIO(image))
      image = prepare_image(image,
        (settings.IMAGE_WIDTH, settings.IMAGE_HEIGHT))

      # ensure our NumPy array is C-contiguous as well,
      # otherwise we won't be able to serialize it
      image = image.copy(order="C")

      # generate an ID for the classification then add the
      # classification ID + image to the queue
      k = str(uuid.uuid4())
      image = helpers.base64_encode_image(image)
      d = {"id": k, "image": image}
      db.rpush(settings.IMAGE_QUEUE, json.dumps(d))

      # keep looping until our model server returns the output
      # predictions
      while True:
        # attempt to grab the output predictions
        output = db.get(k)

        # check to see if our model has classified the input
        # image
        if output is not None:
          # add the output predictions to our data
          # dictionary so we can return it to the client
          output = output.decode("utf-8")
          data["predictions"] = json.loads(output)

          # delete the result from the database and break
          # from the polling loop
          db.delete(k)
          break

        # sleep for a small amount to give the model a chance
        # to classify the input image
        time.sleep(settings.CLIENT_SLEEP)

      # indicate that the request was a success
      data["success"] = True

  # return the data dictionary as a JSON response
  return flask.jsonify(data)

# for debugging purposes, it's helpful to start the Flask testing
# server (don't use this for production
if __name__ == "__main__":
  print("* Starting web service...")
  app.run()
```

## Deep Learning model 

Sau khi dữ liệu được lưu vào trong **Redis** chúng ta cần xử lý nó bằng mô hình Deep Learning sau đó chuyển kết quả trở lại Redis để giúp cho model chỉ cần load một lần mà vẫn có thể xử lý được nhiều request đến. Việc publish trở lại Redis được thực hiện trong file ```run_model_server.py```:

```python
# import the necessary packages
from keras.applications import ResNet50
from keras.applications import imagenet_utils
import numpy as np
import settings
import helpers
import redis
import time
import json

# connect to Redis server
db = redis.StrictRedis(host=settings.REDIS_HOST,
  port=settings.REDIS_PORT, db=settings.REDIS_DB)

def classify_process():
  # load the pre-trained Keras model (here we are using a model
  # pre-trained on ImageNet and provided by Keras, but you can
  # substitute in your own networks just as easily)
  print("* Loading model...")
  model = ResNet50(weights="imagenet")
  print("* Model loaded")

  # continually pool for new images to classify
  while True:
    # attempt to grab a batch of images from the database, then
    # initialize the image IDs and batch of images themselves
    queue = db.lrange(settings.IMAGE_QUEUE, 0,
      settings.BATCH_SIZE - 1)
    imageIDs = []
    batch = None

    # loop over the queue
    for q in queue:
      # deserialize the object and obtain the input image
      q = json.loads(q.decode("utf-8"))
      image = helpers.base64_decode_image(q["image"],
        settings.IMAGE_DTYPE,
        (1, settings.IMAGE_HEIGHT, settings.IMAGE_WIDTH,
          settings.IMAGE_CHANS))

      # check to see if the batch list is None
      if batch is None:
        batch = image

      # otherwise, stack the data
      else:
        batch = np.vstack([batch, image])

      # update the list of image IDs
      imageIDs.append(q["id"])

    # check to see if we need to process the batch
    if len(imageIDs) > 0:
      # classify the batch
      print("* Batch size: {}".format(batch.shape))
      preds = model.predict(batch)
      results = imagenet_utils.decode_predictions(preds)

      # loop over the image IDs and their corresponding set of
      # results from our model
      for (imageID, resultSet) in zip(imageIDs, results):
        # initialize the list of output predictions
        output = []

        # loop over the results and add them to the list of
        # output predictions
        for (imagenetID, label, prob) in resultSet:
          r = {"label": label, "probability": float(prob)}
          output.append(r)

        # store the output predictions in the database, using
        # the image ID as the key so we can fetch the results
        db.set(imageID, json.dumps(output))

      # remove the set of images from our queue
      db.ltrim(settings.IMAGE_QUEUE, len(imageIDs), -1)

    # sleep for a small amount
    time.sleep(settings.SERVER_SLEEP)

# if this is the main thread of execution start the model server
# process
if __name__ == "__main__":
  classify_process()
```

# Khởi chạy server 

Các bạn trước tiên cần khởi chạy file ```run_model_server.py``` trên một screen riêng bằng câu lệnh sau:

```
$ python run_model_server.py
* Loading model...
...
* Model loaded
```

Lúc này Redis đã sẵn sàng lắng nghe các dữ liệu base64 được gửi từ Flask. Việc tiếp theo là cần khởi chạy server Flask trên một screen khác.

```python
$ python run_web_server.py 
Using TensorFlow backend.
 * Loading Keras model and Flask starting server...please wait until server has fully started
...
 * Running on http://127.0.0.1:5000
```

# Testing 

## Sử dụng cURL test Keras REST API

```JSON
$ curl -X POST -F image=@jemma.png 'http://localhost/predict'
{
  "predictions": [
    {
      "label": "beagle", 
      "probability": 0.9461532831192017
    }, 
    {
      "label": "bluetick", 
      "probability": 0.031958963721990585
    }, 
    {
      "label": "redbone", 
      "probability": 0.0066171870566904545
    }, 
    {
      "label": "Walker_hound", 
      "probability": 0.003387963864952326
    }, 
    {
      "label": "Greater_Swiss_Mountain_dog", 
      "probability": 0.0025766845792531967
    }
  ], 
  "success": true
}
```

Chúng ta có thể thấy kết quả như hình sau:

![](https://www.pyimagesearch.com/wp-content/uploads/2018/01/keras_api_result01.jpg)

Các bạn có thể sử dụng REST API này trong các ứng dụng khác như trên Mobile hoặc trên nền Web đều rất hữu ích.


# Tổng kết

Như vậy chúng ta đã cùng tìm hiểu những bước để xây dựng một Web Server chạy model Deep Learning mà không cần dùng giải pháp của bên thứ ba. Rất hi vọng bài viết này giúp anh được cho bạn nhất là những người mới tìm hiểu về lĩnh vực AI. Hẹn găpj lại các bạn trong các bài viết sau.
