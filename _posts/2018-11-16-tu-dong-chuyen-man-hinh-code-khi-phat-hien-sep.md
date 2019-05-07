---
title: "Blog #15 - Ứng dụng AI tự động chuyển màn hình code khi phát hiện sếp đến gần"
last_modified_at: 2017-10-06T16:20:02-05:00
categories:
  - Recommendation
tags:
  - Recommendation System
teaser: 'https://datasciencelab.nl/wp-content/uploads/2018/07/Blog-2.png'

excerpt: 'Xin chào các bạn. Có lẽ sợ sếp là một bệnh thâm niên ở mỗi người làm văn phòng nói chung và đặc biệt là anh em IT nói riêng. Đã bao giờ bạn gặp phải tình huống rất oái oăm khi mà ngồi code cả buổi thì sếp chả ghé thăm, đến lúc vừa rảnh tay lên Youtube nghe nhạc một tý xíu thì sếp đến nhẹ nhàng vỗ vai và thủ thỉ vào tai bạn một câu nói 2 giây nhưng dài như thế kỉ ARE YOU CODING?.'

sidebar:
  nav: "docs"

---
{% include toc %}
Xin chào các bạn. Có lẽ **sợ sếp** là một bệnh thâm niên ở mỗi người làm văn phòng nói chung và đặc biệt là anh em IT nói riêng. Đã bao giờ bạn gặp phải tình huống rất oái oăm khi mà ngồi code cả buổi thì sếp chả ghé thăm, đến lúc vừa rảnh tay lên Youtube nghe nhạc một **tý xíu** thì sếp đến nhẹ nhàng vỗ vai và thủ thỉ vào tai bạn một câu nói 2 giây nhưng dài như thế kỉ **ARE YOU CODING?**.  Thấu hiểu nỗi đau đó của anh em, hôm nay mình mạn phép hướng dẫn các bạn làm một ứng dụng rất hay ho đó là xử dụng AI và các mô hình Deep Learning để qua camera sẽ tự động phát hiện sếp sắp đến lại gần và rồi tự động chuyển ngay màn hình sang chế độ coding rất hữu dụng đặc biệt là cho anh em IT. Xin lưu ý mục đích của bài viết chỉ mang tính chất vui vẻ, giúp anh em cảm thấy đỡ áp lực sau những giờ làm việc căng thẳng. **Hoàn toàn không cổ vũ cho việc mọi người làm việc riêng trong giờ làm.**. OK chúng ta sẽ bắt đầu ngay thôi. Tuy nhiên trước tiên mời bạn xem thử demo dưới đây.


<iframe width="560" height="315" src="https://www.youtube.com/embed/yZdAI1o6p9A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Bước 1: Cách tiếp cận bài toán 
Đối với một bài toán mới chúng ta cần phải phân tích bài toán để tìm ra cách tiếp cận sao cho phù hợp. Tức là phân tích ra **input** và **output** của vấn đề. Đối với bài toán đã nêu ra, mục đích của chúng ta là phát hiện xem khi nào sếp đến (tất nhiên là dựa trên hình ảnh) vậy chắc chắn đầu vào của chúng ta sẽ từ một ảnh khuôn mặt, đầu ra cần phải xác định đó có phải là **sếp** hay không và nếu chúng ta xác định được đó là sếp thì thực hiện một xử lý nào đó (ví dụ như bật màn hình code lên thay vì màn hình đọc báo chẳng hạn). Vậy tựu chung lại chúng ta có thể tổng quát hóa các bước lại như sau:

> * Khoanh vùng được các khuôn mặt 
> * Nhận ra xem khuôn mặt đó có giống sếp hay không 
> * Nếu giống sếp thì bật màn hình code lên (như đang làm việc bình thường)
> * Nếu không phải sếp thì cứ đọc báo tiếp. 

Hai bước sau thì đơn giản rồi phải không, bây giờ chúng ta sẽ bàn luận đến hai bước đầu tiên nhé. Tạm gác lại việc làm sao để khoanh vùng được mặt trong một bức ảnh bởi vì chúng ta không có quà nhiều thời gian. Hơn nữa bài toán này cũng khá quen thuộc nếu như các bạn chịu khó follow các topic về Deep Learning trên Viblo. Chuyển sang bước thứ hai, làm sao để biết được khuôn mặt được khoanh vùng có phải là sếp của mình hay không? Chúng ta cùng tìm hiểu hai cách tiếp cận cho vấn đề này nhé 

## Cách tiếp cận theo Face Verificiation 

Hiểu đơn giản thì cách tiếp cận này sẽ đi trả lời câu hỏi:
> **Với một khuôn mặt này  có giống với sếp mình hay không và nếu giống thì giống bao nhiêu phần trăm**. 
 
 
Ở đây chúng ta đơn thuần đi so sánh (compare) khuôn mặt mới với một khuôn mặt cũ đã có trong cơ sở dữ liệu (ví dụ các ảnh của sếp) xem hai bức ảnh này giống nhau bao nhiêu phần trăm. Thông thường bài toán này dẫn chúng ta đến một bài toán khác là làm thế nào để xác định được hai khuôn mặt này có giống nhau hay không. Như chúng ta đã biết máy tính chỉ hoạt động trên số, và tất cả cá giải thuật về Deep Learning cũng đều quy về việc xử lý trên không gian ma trận thực. Chính vì thế chúng ta cần một cách nào đó để mã hóa một ảnh của chúng ta thành vector gọi là **embeding**. Chúng ta có thể xem sơ đồ xử lý như sau:
 
 ![](https://datasciencelab.nl/wp-content/uploads/2018/07/Blog-2.png)
 
 Trên hình chúng ta thấy nhiệm vụ của **Face Embedding Model** chính là chuyển đổi từ hình ảnh sang một vector số thực. Để làm được điều này thường người ta sử dụng mạng nơ ron với hàm loss là một **Triplet loss**. Mọi người có thể tìm hiểu thêm về kĩ thuật này trong các bài viết khác trên Viblo 
 
 ![](data:image/jpeg;base64,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)
 
 Hiểu đơn giản đó là việc chúng ta đưa những ảnh có nội dung giống nhau lại gần nhau và ảnh có nội dung khác nhau ra xa nhau. Mọi người có thể tìm hiểu thêm về phương pháp này trên các bài viết về Deep Learning trên Viblo. Giờ chúng ta sẽ cùng tìm hiểu phương pháp tiếp theo. 
## Cách tiếp cận theo Face Recognition 

Thay vì việc phải tính toán một độ tương tự và so sánh như cách tiếp cận đầu tiên, chúng ta sẽ định nghĩa một mô hình và câu trả lời **output** của nó chính là xác suất của khuôn mặt có phải là sếp hay không. Việc này được giải quyết khá đơn giản và hiệu quả bởi mạng nơ ron tích chập (CNN) chúng ta có thể thấy trong mô hình sau:

![](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/img/pipeline.png)

Lúc này mạng của chúng ta có thể trả lời luôn câu hỏi rằng

> **Đây là ai? - Output là sếp hoặc không phải là sếp**
OK sau khi đã hiểu một vấn đề chúng ta sẽ tiến hành lựa chọn một trong hai phương pháp để tính toán. Trong bài viết này mình sẽ sử dụng phương pháp thứ hai và các bạn có thể thử cài đặt phương pháp thứ nhất xem sao. Mình nghĩ là không có nhiều khó khăn lắm đâu. OK chúng ta bắt đầu nhé

# Bước 2: Chuẩn bị dữ liệu. 

Đối với mỗi một bài toán Machine Learning nào đều cần phải chuẩn bị về mặt dữ liệu. Nếu không có dữ liệu thì sẽ không có gì cả. Các bạn hãy thu thập các dữ liệu mặt của sếp mình, càng nhiều càng đa dạng càng tốt, Kiểu đa sắc thái như thế này là một nguồn dữ liệu rất quý giá. 

![](https://images.viblo.asia/d1e5f7ad-e43e-4ad7-9226-0cd3b48828ed.png)

Sau đó thu thập dữ liệu của các loại mặt khác không phải là mặt của sếp mình cho tất cả vào một folder chẳng hạn. Lúc này chúng ta sẽ có hai folder có tổ chức như sau:


![](https://images.viblo.asia/c25df967-fa9f-444b-92c7-488ddbae509f.png)

Càng bạn lưu ý rằng nên thu thập nhiều ảnh một chút model sẽ chính xác hơn 

# Bước 3:  Tiền xử lý dữ liệu  
Đây là một bước khá quan trọng trong khi thực hiện một bài toán Deep Learning nào. Chúng ta đã biết rằng **Garbage in - Garbage out** chính vì thế nên việc đưa dữ liệu vào trong mô hình cũng cần phải được xử lý một cách kĩ lưỡng. Chúng ta có một vài thao tác xử lý dữ liệu như sau:

* Resize image 
* Chuyển về gray scale (nếu cần)
* Normalization image - chuẩn hóa ảnh giúp cho việc training được cải thiện về tốc độ và độ chính xác 
* Augumentation image - giúp sinh thêm các dữ liệu mới, làm giàu hơn tập dữ liệu đã có 
* Loại bỏ các dữ liệu nhiễu giúp mô hình không bị **lệch**
* Cân bằng lại dữ liệu giúp cho mô hình học được tổng quát hơn

Trong bài viết này chúng ta sử dụng **Keras** và model Mobilenet để training nên các bước tiền xử lý dữ liệu này chúng ta sử dụng trực tiếp của Keras luôn. Tiến hành import các thư viện cần thiết:

```python
# Import dependency 
import os 
import cv2
import keras
import numpy as np
from keras import backend as K
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from keras.layers import Dense, GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input
from IPython.display import Image
from keras.optimizers import Adam
```

Và định nghĩa các tham số 

```python
# Define parameters
IMAGE_SIZE = 224
IMAGE_DATA = './data'

images = []
labels = []
```

Sau đó chúng ta định nghĩa hàm ```preprocess``` như sau:


```python
def prepare_image(file):
    img_path = ''
    img = image.load_img(img_path + file, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

```
Và đoạn code để sinh dữ liệu mẫu dùng cho việc training như sau:


```python
# Generate dataset

for path, subdirs, files in os.walk(IMAGE_DATA):
    for name in files:
        img_path = os.path.join(path, name)
        images.append(prepare_image(img_path))
        labels.append(path.split('/')[-1])
```

# Bước 4: Định nghĩa mô hình
Giống như đã mô tả ở trên chúng ta sử dụng mô hình Mobilenet để dự đoán mặt vào có phải là sếp hay không. Mình sẽ không nhắc lại lý thuyết về CNN nữa vì nó đã xuất hiện quá nhiều trên Viblo cũng như các diễn đàn khác. Các bạn có thể tìm hiểu nhé. 

Khai báo mô hình đơn giản với Keras như sau:

```python 
model = keras.applications.mobilenet.MobileNet(classes=2, weights=None)
```

Mọi người có thể sử dụng ```model.summary()``` để hiển thị số lượng các tham số của mô hình 

![](https://images.viblo.asia/3278295f-a10d-4b13-b730-dffac4ced756.png)
## Mapping label  
Vì mô hình của chúng ta là mô hình phân loại nên chúng ta sẽ cần sử dụng hàm loss là **cross_entropy** để tính toán. Chính vì thế nên việc đầu tiên là chuyển các class từ **boss** thành 1 và **other** thành 0.  Chúng ta thực hiện như sau 

```python 
# Mapping label

mapped_labels = list(map(lambda x: 1 if x == 'boss' else 0, labels))

from keras.utils import np_utils

y_data = np_utils.to_categorical(mapped_labels)
```

# Bước 5:  Phân chia dữ liệu 
Chúng ta sử dụng thư viện **train_test_split** để tiến hành phân chia dữ liệu thành hai tập training và testing. Giống như bao bài toán khác
```python 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(images, y_data, test_size=0.2)
```

# Bước 6:  Training thuật toán 

Giờ là lúc chúng ta dạy cho mô hình biết được đâu là boss và đâu không phải là boss rồi đấy. Có một lưu ý là do mạng Mobilenet là một hàm khá lớn dù là 2 classs nhưng số lượng tham số cũng lên đến **3,230,914** nên chúng ta cần sử dụng nhiều dữ liệu hơn để tránh bị Overfiting khiến cho mô hình kém hiệu quả. Dù sao thì dữ liệu vẫn là yếu tố quan trọng nhất phải không các bạn. Tiếp theo chúng ta cần complie mô hình 
## Complie mô hình 
```python 
model.compile(loss='categorical_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])
```
## Đặt checkpoint 

Việc đặt checkpoint rất quan trọng trong quá trình training mô hình. Giúp chúng ta lưu lại được mô hình tốt nhất theo một tiêu chí nào đó ví dụ như **val_loss** hay **val_accuracy** cũng là cách để chúng ta phòng tránh trường hợp đang training thì mất điện hay muốn training tiếp trong lần sau mà không cần training lại từ đâu. Tóm lại là phải viết checkpoint vào không mất mô hình đừng kêu

```python 
from keras.callbacks import ModelCheckpoint

model_file = "boss_model/model_mobilenet.hdf5"

checkpoint = ModelCheckpoint(model_file, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
```

## Training

Sau cùng là bước training 

```python 
model.fit(x=X_train, y=y_train, batch_size=16, epochs=100, verbose=1, validation_data=(X_test, y_test), callbacks=callbacks_list)
```

Các bạn cứ đợi và theo dõi thôi nhé. Do tập dữ liệu của mình nhỏ khoảng 750 ảnh nên việc training cũng sẽ diễn ra rất nhanh thôi. Đây là kết quả training trên máy của mình sau vài epochs 

```python 
Epoch 1/100
750/750 [==============================] - 5s 37ms/step - loss: 0.3298 - acc: 0.8667 - val_loss: 0.0221 - val_acc: 1.0000

Epoch 00001: val_loss improved from inf to 0.02205, saving model to boss_model/model_mobilenet.hdf5
Epoch 2/100
750/750 [==============================] - 3s 7ms/step - loss: 0.0143 - acc: 0.9600 - val_loss: 0.0159 - val_acc: 0.9465

Epoch 00002: val_loss improved from 0.02205 to 0.01592, saving model to boss_model/model_mobilenet.hdf5
Epoch 3/100
750/750 [==============================] - 3s 7ms/step - loss: 0.0017 - acc: 0.9952 - val_loss: 0.0027 - val_acc: 0.9815

```

# Bước 7: Chuẩn bị mô hình cho deploy 
## Lưu mô hình 
Sau khi tiến hành traininig lại mô hình nhiều lần chúng ta sẽ thu được một mô hình **tốt nhất** và sử dụng nó để deploy lên hệ thống thực. Việc này được thực hiện như sau:


```python 
model.save('boss_model/final_model.h5')
```
## Load lại mô hình 
Và sau đó các bạn thử load lại mô hình này và predict một vài mẫu dữ liệu xem sao nhé:

```python 
from keras.models import load_model
import keras
from keras.utils.generic_utils import CustomObjectScope

# Load pretrained model
with CustomObjectScope({'relu6': keras.applications.mobilenet.relu6,'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D}):
    model = load_model('./boss_model/final_model.h5')
```

Một lưu ý là chúng ta cần phải chạy qua các bước tiền xử lý khi dự đoán, giống hệt lúc chúng ta training. 

# Bước 8: Deploy bằng OpenCV 

## Xử lý model để dự đoán 

Việc đầu tiên cần làm là  Tạo file boss_model.py.  Chúng ta sử dụng file này để load model đã được lưu từ các bước trên bao gồm cả các hàm về xử lý dữ liệu và dự đoán kết quả 

```python 

import cv2
import keras
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.utils.generic_utils import CustomObjectScope
# Load pretrained model

with CustomObjectScope({'relu6': keras.applications.mobilenet.relu6,'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D}):
    model = load_model('./model/model.h5')

IMAGE_SIZE=224

def prepare_image(img):
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

def predict(img):
    """
    Predict face crop from frame
    :param img:
    :return: If boss is appear when open the code IDE
    """
    try:
        img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE), interpolation=cv2.INTER_AREA)
        probs = model.predict(prepare_image(img))
        is_boss = np.argmax(probs[0])
        return is_boss
    except:
        return False

```

## Detect khuôn mặt bằng dlib 

Giống như mô tả ở phái đầu tiên của bài viết, trong quá trình dự đoán chúng ta cần phải detect khuôn mặt và sử dụng một thư viện rất nổi tiếng đó là dlib. Quá trình xử lý của nó như sau:

```python 
import dlib
hog_face_detector = dlib.get_frontal_face_detector()
faces_hog = hog_face_detector(image)
```
Kết quả của nó như sau:

![](https://cdn-images-1.medium.com/max/1200/1*cksGOuQIvvfqjJIGx69amw.png)

## Sử dụng OpenCV để stream dữ liệu từ Webcam 

Chúng ta cần sử dụng dữ liệu stream từ webcam để theo dõi **sếp** và phát hiện ra khi nào sếp đến gần một cách tức thời. Việc này có thể thực hiện bằng cách sử dụng webcam và OpenCV để stream dữ liệu.  Về cơ bản chúng ta có thể thực hiện nó như sau :


```python 
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        # Excute frame here 
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()
```

## Xử lý crop mặt và dự đoán 
Chúng ta sẽ crop từng khuôn mặt trong từng frame và dự đoán kết quả. Nếu là boss thì thực hiện mở ngay cửa sổ code 
```python 
    if ret:
        # Resize window
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', 400, 400)
        # Resize frame for decrease predict time
        scale = 0.5
        resize_frame = cv2.resize(frame, (int(frame.shape[1]*scale), int(frame.shape[0]*scale)))
        faces_hog = hog_face_detector(resize_frame)
        frame_h, frame_w, _ = frame.shape
        reindex_x = lambda x: max(min(x, frame_w), 1)
        reindex_y = lambda x: max(min(x, frame_h), 1)

        # loop over detected faces
        for face in faces_hog:
            x = reindex_x(int(face.left() / scale))
            y = reindex_y(int(face.top() / scale))
            r = reindex_x(int(face.right() / scale))
            b = reindex_y(int(face.bottom() / scale))

            # draw box over face
            crop_face = frame[x: r, y: b]
            is_boss = predict(crop_face)
            if is_boss:
                cv2.putText(frame, "BOSS", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (0, 0, 255), 4)
                cv2.rectangle(frame, (x, y), (r, b), (0, 0, 255), 2)
                boss_count += 1
                # Open your IDE application for coding
                if boss_count > 3:
                    os.system('open -a "PyCharm CE"')
                    boss_count = 0
            else:
                cv2.putText(frame, "NORMAL", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (0, 255, 0), 4)
                cv2.rectangle(frame, (x, y), (r, b), (0, 255, 0), 2)
```

Mọi người có thể tham khảo kĩ hơn source code trong file này tại [đây](https://github.com/thandongtb/boss_detection/blob/master/detect_camera.py)

# Source code 

Các bạn có thể tham khảo source code của bài viết tại [đây](https://github.com/thandongtb/boss_detection/)

Cảm ơn các bạn đã theo dõi bài viết hẹn gặp lại trong những bài viết tiếp theo.
            