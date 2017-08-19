---
title: "Blog #2 - Cái máy nó học như thế nào"
last_modified_at: 2017-08-29T16:20:02-05:00
categories:
  - Introduction
tags:
  - How To Learning
  - Machine Learning Workflow
teaser: 'http://lazi.vn/uploads/dhbc/1481886288_Hoc_Vet.jpg'

excerpt: 'Lần đầu tiên nghe thấy khái niệm về Machine Learning tôi cũng không khỏi "hoang mang style" bởi cái thuật ngữ này và tôi biết có khá nhiều người mới bắt đầu cũng có cảm giác tương tự. Tôi cứ tưởng máy tính chỉ có thể bảo gì làm nấy thôi chứ sao có thể "học" được... Nếu các bạn cũng có những suy nghĩ như vậy thì bài viết này sẽ giải thích chi tiết cho bạn Làm thế nào máy có thể học và các bước cơ bản khi thực hiện một bài toán Machine Learning là như thế nào.'

sidebar:
  nav: "docs"

---
{% include toc %}

# Giới thiệu

Lần đầu tiên nghe thấy khái niệm về Machine Learning tôi cũng không khỏi "hoang mang style" bởi cái thuật ngữ này và tôi biết có khá nhiều người mới bắt đầu cũng có cảm giác tương tự. Tôi cứ tưởng máy tính chỉ có thể bảo gì làm nấy thôi chứ sao có thể "học" được... Nếu các bạn cũng có những suy nghĩ như vậy thì bài viết này sẽ giải thích chi tiết cho bạn Làm thế nào máy có thể học và các bước cơ bản khi thực hiện một bài toán Machine Learning là như thế nào. OK chúng ta bắt đầu thôi

# Vì sao máy tính có thể học

Có lẽ từ **học** không còn xa lạ gì đối với mỗi chúng ta nữa. Ngay từ khi sinh ra chúng ta đã phải học rất rất nhiều thứ như học ăn, học uống, học nói, học đọc, học viết... Nhớ lại những thời tôi đi học tôi thường sợ nhất là môn **Lịch sử** và không hiểu vì sao mà kiến thức lịch sử của tôi chỉ tồn tại trong đầu đúng từ tối hôm trước cho đến hết tiết Sử của ngày hôm sau, ngay sau khi cô giáo kiểm tra xong bài cũ là tôi cũng quên hết sạch. Rõ ràng đối với mỗi chúng ta người ta phân biệt hiện tượng **học vẹt** và sự thông minh thực sự. Và các bạn cũng sẽ thấy trong học máy cũng có những khái niệm như vậy.

![](http://lazi.vn/uploads/dhbc/1481886288_Hoc_Vet.jpg)

## Machine Learning khác với if...else

Nếu bạn coi rằng người có trí nhớ tốt thì có khả năng học giỏi thì cũng có vẻ hợp lý vì với con người thì trí nhớ tốt đồng nghĩa với sự thông minh. Nhưng đừng nhầm lẫn với anh bạn **máy tính** nhé. Với những ổ **SSD** hàng **Petabyte** thì gần như trí nhớ của chúng là vô hạn tuy nhiên điều này chẳng liên quan gì đến việc một chiếc máy có **thông minh** thực sự hay không cả.

Hãy tưởng tượng bạn làm một **chat bot nhắn tin cho người yêu** bằng cách thu thập các đoạn hội thoại của các đôi tình nhân. Bộ nhớ của máy tính tầm vài **TB** đủ cho bạn lưu hàng tỉ cuộc hội thoại như thế. Tuy nhiên có hai hướng tiếp cận cho vấn đề này.

![](https://www.nanorep.com/wp-content/uploads/2016/12/blog-post-definitive-guide-to-chat-bot-strategy-770x385.png)

> **Cách 1**
>
**if** Q  in questions **then** print answer  of Q **else** return Null

Cách này có nghĩa là bạn sẽ phải **tìm kiếm chính xác** câu hỏi của người hỏi trong tập dữ liệu và trả lời lại với answer tương ứng. Điều này chính là cách nghĩ cơ bản trong lập trình. Tuy nhiên nó hoàn toàn thất bại nếu như tập dữ liệu không đủ lớn, chưa kể rằng nó sẽ chẳng thể nào đem lại những cảm giác thú vị cho người dùng vì những câu trả lời bị lặp lại một cách **nhàm chán**. Giống y như việc mình học lịch sử hồi xưa vậy. Rõ ràng chiếc máy tính này đang **học vẹt** và không hề có một chút **Machine Learning** nào trong này cả. Một hệ thống **chatbot thông minh** sẽ không làm như thế.

Một hệ thống **chatbot thông minh** sẽ biết cách tự **suy diễn** xem với mỗi câu hỏi nào thì nên trả lời thế nào. Cũng giống như việc con người sẽ giải quyết được nhiều vấn đề hơn thông qua suy luận chứ không phải dựa trên sự **học tủ, học vẹt** nữa.


##  Cái máy nó học thế nào

Hãy tưởng tượng lại xem hồi bé chúng ta được bố mẹ dạy nhận biết đồ vật từ cái ca đến con bò con chó như thế nào. Ban đầu chúng ta còn ngập ngừng chưa biết được hết mặt các con vật nhưng sau đó chúng ta gặp lại càng nhiều lần thì không còn bỡ ngỡ nữa. Các trường mẫu giáo cũng hay sử dụng các **Flash card** để dạy trẻ con nhận biết đồ vật.

![](http://cdn.nhanh.vn/cdn/store/3198/artCT/8462/2_letter.jpg)

Mọi người thấy không, muốn học được một điều gì đó thì phải có người **dạy** và muốn **máy có thể học** thì chúng ta cũng cần phải dạy nó. Nhưng trước tiên muốn dạy được nó chúng ta cần phải có một **tập dữ liệu**, hiểu đơn giản giống như việc chúng ta phải có **con bò, con chó** thật hoặc có tranh ảnh về chúng thì mới có hi vọng dạy được đứa trẻ vậy.  Khá dễ hiểu phải không bạn. Hãy nhớ rằng:

> Không có dữ liệu thì sẽ không học được

Tuy nhiên việc có dữ liệu chuẩn rồi thì vấn đề tiếp theo đó chính là **chọn một người thầy tốt**. Rõ ràng rằng chúng ta sẽ không thể học được điều gì hay ho từ một ông thầy kém hiểu biết cả. Đối với máy cũng có những **thầy giáo** để dạy cho nó phải học cái gì từ tập dữ liệu của mình và những thầy giáo đó chính là các **thuật toán học máy**.  Việc lựa chọn một ông thầy dạy cho con hay điều mà tôi muốn ám chỉ là việc lựa chọn một giải thuật tốt cho một bài toán học máy là một bước khá quan trọng. Có một lưu ý rằng:

> Không phải cứ thuật toán phức tạp là hiệu quả sẽ cao

Việc lựa chọn thuật toán còn phụ thuộc vào bản thân của **tập dữ liệu** đối với những tập dữ liệu đơn giản, ít **feature** thì không cần phải training bằng một thuật toán quá phức tạp.  Cũng giống như không ai lấy một **giáo sư về Machine Learning** để đi dạy trẻ con nhận biết đồ vật qua Flash card cả. Vậy nên trong Machine Learning không có khái niệm thuật toán này tốt, thuật toán kia không tốt. Mỗi thuật toán đều có cái ưu và nhược điểm riêng đối với từng tập dữ liệu. Việc áp dụng và phát huy nhó như thế nào là việc của mỗi chúng ta.



# Machine Learning Workflow

Tôi đã thảo luận với các bạn cách dạy máy học như thế nào. Giờ tôi sẽ nói với các bạn về các bước thực hiện một bài toán **Machine Learning**. Tựu chung lại thì Machine Learning có thể được chia làm ba bước chính như sau:

> * **Modeling**: là bước mô hình hóa bài toán. Với mỗi một loại bài toán lại có một mô hình phù hợp như **hồi quy** hoặc **phân lớp** hoặc **tuyến tính** hoặc **phi tuyến tính**. Nhắc lại một lần nữa **TÙY YÊU CẦU BÀI TOÁN**. Sau bước này ta sẽ tìm ra được một số thuật toán phù hợp cho bước tiếp theo.

> * **Learning**:  sau khi đã lựa chọn được thuật toán thì bước tiếp theo đó chính là bước **học** tức là sử dụng thuật toán đó để **training**  trên tập dữ liệu đã cho. Sau bước này chúng ta thu được một bộ tham số được  gọi là **model**


> * **Predicting**:  sau khi có **model** chúng ta sử dụng nó để dự đoán các **dữ liệu mới**. Mọi người lưu ý rằng các **dữ liệu mới** này phải là các dữ liệu **CHƯA ĐƯỢC TRAINING BAO GIỜ** thì mới có thể sử dụng để đánh giá độ tốt của **model** thu được.

Đó là 3 bước chính, ngoài ra còn một số bước tiền xử lý dữ liệu được thực hiện giống như sơ đồ sau:

![](https://mapr.com/ebooks/spark/images/mllib_rec_engine_image006.png)

Nó có thể giải thích kĩ hơn như sau:

* Từ người dùng ta thu thập được **dữ liệu**
* Từ dữ liệu ta tiến hành **tiền xử lý** làm sạch dữ liệu
* Sau khi tiền xử lý ta **modeling** lựa chọn giải thuật
* Sau đó ta tiến hành **tách dữ liệu** thành hai tập **train** và **test**
* Sau đó ta tiến hành **thay đổi giải thuật** cho đến khi có kết quả tốt nhất
* Lựa chọn mô hình tốt nhất để trả lại **feedback** cho người dùng

## Ví dụ minh họa

Chúng ta sẽ cùng tìm hiểu về các bước làm bài toán Machine Learning thông qua ví dụ minh họa cho bài toán **phân loại hoa** với ngôn ngữ **Python**. Và tôi cũng sẽ sử dụng **Python** làm ngôn ngữ chính cho tất cả các ví dụ trong blog này của tôi.  Bây giờ chúng ta sẽ bắt đầu từng bước nhé


### Giới thiệu bài toán

Dựa trên một tập dữ liệu về các đặc điểm của bông hoa, tôi sẽ sử dụng **Machine Learning** để dự đoán xem nó là loài hoa nào. Đây là một bài toán **phân lớp** hay trong tài liệu tiếng anh gọi là **classification**.

### Tập dữ liệu

Do mục đích để minh họa nên tôi sử dụng một tập dữ liệu mẫu khá nổi tiếng cho bài toán này đó chính là tập dữ liệu hoa [Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set)

Tập dữ liệu này bao gồm 3 class tương ứng với số liệu của ba họ hoa **iris** được mô tả trong hình sau:

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAniZY3Z_Kr6zXHzHG4fzk70RaiRQSQsVD_4qa8BPofRzZ8pHE)

Chính vì tập dữ liệu đã được **chuẩn hóa** và được sử dụng nhiều cho mục đích nghiên cứu nên tôi bỏ qua bước **tiền xử lý dữ liệu**  đối với tập dữ liệu này. Mặc dù trên thực tế thì quả thực là **đời không như mơ**. Thậm chí bước tiền xử lý dữ liệu là bước tốn nhiều thời gian và công sức nhất trong quá trính làm **Machine Learning**.  Giờ đã xong bước tiền xử lý dữ liệu, chúng ta sẽ đến bước tiếp theo đó là **lựa chọn thuật toán**.

### Lựa chọn thuật toán

Do bài toán này thuộc vào dạng **classification** nên chúng ta sẽ thử sử dụng một vài phương pháp thông dụng trong phân lớp như **SVM** hay **Random Forest** hay **Naive Bayes** hoặc cao siêu hơn một chút như **Neural Network** để áp dụng lên bài toán này. Giờ chúng ta sẽ tiến hành sử dụng Python để minh họa một số giải thuật nói trên

### Minh họa bằng Python

Chúng ta đã định hướng trước sẽ sử dụng một số thuật toán trong **classification** để giải quyết bài toán phân loại hoa với bộ dữ liệu  [Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set). Bây giờ chúng ta sẽ học cách triên khai nó trên Python với bộ thư viên [Sklearn](http://scikit-learn.org/stable/index.html) vô cùng hữu ích. Trong bộ thư viện này bộ dữ liệu hoa **iris** đã được build-in sẵn rồi chúng ta chỉ việc lấy ra sử dụng thôi.

Đầu tiên là import nó vào

```
from sklearn.datasets import load_iris
```

Sau đó thì làm thế nào nhỉ. Chúng ta cùng thử xem nó hoạt động chưa bằng hàm **main** như sau:

```
if __name__ == "__main__":
    iris = load_iris()
    print "Size of data", iris.data.shape
```
Câu lệnh trên in ra kết quả là
```
Size of data (150, 4)
```
Có nghĩa là data của chúng ta bao gồm **150** bông hoa với 4 thuộc tính của mỗi bông hoa. Để in các **class** tương ứng với mỗi bông hoa chúng ta làm như sau:

```
print "Target", iris.target
```

Chúng ta sẽ thấy đươc các **class** tương ứng là `[0, 1, 2]` với ba loại hoa iris mô tả ở phần trên.

Bước tiếp theo chúng ta cần làm đó là **tách tập dữ liệu** thành hai phần **training** và **testing**. Chúng ta sử dụng thư viện `train_test_split`  của `sklearn`  như sau:

```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
```

Đoạn code trên tách tập dữ liệu với `ratio = 0.2` tức là `80%` để **training** và `20%` dùng để **testing**

Tiếp theo chúng ta sẽ áp dụng thử một thuật toán phân lớp đó là **SVC với kernel tuyến tính** thuộc bộ thư viện `sklearn`

```
from sklearn import svm
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
```

Sau khi chạy xong đoạn code trên chúng ta đã lưu được một **model** sử dụng để dự đoán. Lưu ý là **model** này mới chỉ được sinh ra trên **tập training**. Chúng ta cần kiểm tra kết quả dự đoán với tập dữ liệu **testing**. Tôi hay sử dụng thư viện `classification_report` để in kết quả phân lớp. Xây dựng hàm in kêt quả như sau:

```
def evaluate_model(X_test, y_test):
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
```

Và trong hàm**main** chúng ta thêm vào đoạn code sau đoạn **training** như sau:

```
# Evaluate SVC
evaluate_model(X_test, y_test)
```

Tiến hành chạy thử **model** thu được kết quả:

![](http://sv1.upsieutoc.com/2017/08/31/Screenshotfrom2017-08-31193002.png)

Ở đây có hai chỉ số các bạn cân quan tâm đó chính là **precision** và **recall** ta định nghĩa chúng như sau:

> **Precision** bao nhiêu **cái đúng được lấy ra**

Một cách toán học thì

$$Precision=\frac{y_{true} \cap  y_{selected}}{y_{selected}}$$

> **Recall** bao nhiêu cái **được lấy ra là đúng**

Hay tức là

$$Recall=\frac{y_{true} \cap  y_{selected}}{y_{true}}$$

Từ đó chỉ số thứ 3 ở trên `f1-score` được định nghĩa là:

$$2.\frac{Precision.Recall}{Precision+Recall}$$

Giờ chúng ta sẽ thử nghiệm mô hình với một số thuật toán khác trên cùng một tập dữ liệu để đánh giá được hiệu năng của từng thuật toán. Ở đây tôi sẽ so sánh với các thuật toán **Random Forest**, **Naive Bayes** còn về **Neural Network** xin hẹn các bạn một dịp sau.

## Full Code

Các bạn có thể tham khảo **Full code** của bài viết này [tại đây](https://github.com/tuhocmachinelearning/tuhocmachinelearning.github.io/blob/master/code/blog_2.py)

## Kết quả
Sau đây là kết quả chúng ta **estimate** sau khi training xong cả 3 model với cùng một tập dữ liệu

![](http://sv1.upsieutoc.com/2017/08/31/Screenshotfrom2017-08-31195405.png)

Chúng ta thấy rằng 3 model trên cùng một tập dữ liệu thì **SVC** cho kêt quả tốt nhất và **Naive Bayes** cho kết quả kém nhất. Bằng việc so sánh các phương pháp này chúng ta sẽ lựa chọn được model tốt hơn. Sau khi lựa chọn được model chúng ta sẽ lưu lại model tốt nhất để sử dụng cho lần sau.

# Tổng kết

Qua bài viết này tôi đã cùng các bạn trao đổi về cách thực hiện một bài toán **Machine Learning** cơ bản. Rất hi vọng được các bạn ủng hộ để tôi có nhiều động lực viết thêm những chủ đề hay và bổ ích hơn. Một lần nữa cảm ơn các bạn rất nhiều vì đã theo dõi [Blog Tự học Machine Learning](https://tuhocmachinelearning.github.io/))

Trân trọng

[Phạm Văn Toàn](https://www.facebook.com/thienan.pham.710)

