---
title: "Blog #10 - Một vài hiểu nhầm khi mới học Machine Learning"
last_modified_at: 2017-10-06T16:20:02-05:00
categories:
  - Recommendation
tags:
  - Recommendation System
teaser: 'https://cdn-images-1.medium.com/max/1600/1*qxJGuGBZiNXotX3Q41nomw.png'

excerpt: 'Xin chào các bạn, đã lâu lắm rồi tôi mới có dịp được viết một bài chia sẻ với các bạn về chủ đề vô cùng quen thuộc đó là Machine Learning. Sau một thời gian làm về Machine Learning tôi nhận thấy có một vài vấn đề mà không ít người mới học hay ngay cả những người đã từng làm rất lâu trong lĩnh vực này cũng đang bị nhầm lẫn. Chính vì lẽ đó tôi xin được mạn phép viết một bài viết nêu lên một số khái niệm dễ gây nhầm lẫn cho mọi người. OK giờ chúng ta bắt đầu nhé'

sidebar:
  nav: "docs"

---
{% include toc %}

Xin chào các bạn, đã lâu lắm rồi tôi mới có dịp được viết một bài chia sẻ với các bạn về chủ đề vô cùng quen thuộc đó là **Machine Learning**. Sau một thời gian làm về **Machine Learning** tôi nhận thấy có một vài vấn đề mà không ít người mới học hay ngay cả những người đã từng làm rất lâu trong lĩnh vực này cũng đang bị nhầm lẫn. Chính vì lẽ đó tôi xin được mạn phép viết một bài viết nêu lên một số **khái niệm** dễ gây **nhầm lẫn** cho mọi người. OK giờ chúng ta bắt đầu nhé

# Model parameter và model hyperparameter?

Nếu các bạn làm **Machine Learning** một thời gian đủ lâu thì cũng không còn lạ lẫm gì với hai khái niệm này nữa tuy nhiên đôi khi có một vài tài liệu viết không được rõ ràng về vấn đề này, hay nói đúng hơn là sử dụng hơi tuỳ tiện khiến những người mới đọc và làm **Machine Learning** cảm thấy sốc và choáng vì thấy có những chỗ thì gọi là **tối ưu parameter** trường hợp khác lại gọi là **lựa chọn hyperparameter** và ngược lại thật là **loạn cào cào**. Mình xin mạn phép được giải thích kĩ hơn hai khái niệm này và từng trường hợp cụ thể tránh sau này chúng ta sử dụng thuật ngữ không đúng.

## Model parameter là gì

![](https://cdn-images-1.medium.com/max/1600/1*qxJGuGBZiNXotX3Q41nomw.png)

Quay về bản chất của **Machine Learning** một chút, đầu tiên để làm về **học máy** chúng ta cần phải có một **tập dữ liệu** - muốn nói gì thì nói chứ không có dữ liệu chúng ta sẽ lấy cái gì mà học với chả hành đúng không? Sau khi có dữ liệu rôi thì việc cần làm của **máy** là tìm ra một mối liên hệ nào đó trong cái đống dữ liệu này. Giả sử dữ liệu của chúng ta là thông tin về thời tiết  như độ ẩm lượng mưa nhiệt độ... và yêu cầu cho máy thực hiện là tìm mối liên hệ giữa các yếu tố trên và việc **người yêu có giận ta hay không giận?**. Nghe thì có vẻ không liên quan lắm nhưng việc cần làm của máy học đôi khi là những thứ khá vớ vẩn như vậy đó.  Bây giờ giả sử chúng ta sử dụng biến $y$ để biểu diễn việc **người yêu có giận hay không giận?** các biến $x_1, x_2, x_3 ...$ đại diện cho các yếu tố thời tiết. Chúng ta quy một liên hệ về việc tìm hàm $f(x)$ như sau:


$$y=f(x)=w_1.x_1 + w_2.x_2 + w_3.x_3$$

Các bạn có thấy các hệ số $w_1, w_2, w_3 ..$ không?  Đó chính là **mối liên hệ** giữa đống dữ liệu và yếu tố chúng ta đang yêu cầu đó, chính các hệ số này được gọi là **Model Parameter** đó. Như vậy chúng ta có thể định nghĩa **model parameter** như sau:

> **Model Parameter** là các giá trị của model được sinh ra từ dữ liệu huấn luyện giúp thể hiện mối liên hệ giữa các đại lượng trong dữ liệu

Như vậy khi chúng ta nói **tìm được mô hình tốt nhất cho bài toán** thì nên ngầm hiểu rằng chúng ta đã tìm ra được các **Model parameter** phù hợp nhất cho bài toán trên tập dữ liệu hiện có. Nó có một số đặc điểm như sau:

* Nó được sử dụng để dự đoán đối với dữ liệu mới
* Nó thể hiện sức mạnh của mô hình chúng ta đang sử dụng. Thường được thể hiện bằng tỷ lệ **accuracy** hay chúng ta gọi là độ  chính xác
* Được **học** trực tiếp từ tập dữ liệu huấn luyện
* Thường **không** được đặt thủ công bởi con người

**Model paramter** có thể bắt gặp trong một số dạng như là các trọng số trọng mạng nơ ron, các **support vectors** trong SVM hay các **coefficients** trong các giải thuật linear regression hoặc logistic regression...


## Model Hyperparameter là gì?

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2yKsmBgbMkhzSurl12jDAzvkUWFza_T-SYzgAC6kn-T75StYf)

Có lẽ do thời quen thường dịch **Hyperparameter** là **siêu tham số** nên chúng ta thường ngầm định nó giống **Model Parameter** nhưng có phần **khủng hơn**. Thực ra hai khái niệm này là hoàn toàn tách biệt. Nếu như **Model parameter** được mô hình sinh ra từ chính tập dữ liệu huấn luyện thì **Model Hyperparameter** lại hoàn toàn khác. Nó hoàn toàn **nằm ngoài** mô hình và không phụ thuộc và tập dữ liệu huấn luyện. Như vậy mục đích của nó là gì? Thực ra chúng có một vài nhiệm vụ như sau:

* Được sử dụng trong quá trình huấn luyện, giúp mô hình tìm ra được các **parameters** hợp lý nhất
* Nó thường được lựa chọn thủ công bởi những người tham gia trong việc huấn luyện mô hình
* Nó có thể được định nghĩa dựa trên một vài chiến lược **heuristics**

Chúng ta hoàn toàn không thể biết được đối với một bài toán cụ thể thì đâu là **Model Hyperparameter** tốt nhất. Chính vì thế trong thực tế chúng ta cần sử dụng một số kĩ thuật để ước lượng được một khoảng giá trị tốt nhất (Ví dụ như hệ số $k$ trong mô hình **k Nearest Neighbor**) như **Grid Search** chẳng hạn.

Sau đây mình xin đưa một vài ví dụ về **Model Hyperparameter**:
* Chỉ số **learning rate**  khi training một mạng nơ ron nhân tạo
* Tham số $C$ và $sigma$ khi training một **Support Vector Machine**
* Hệ số $k$ trong mô hình **k Nearest Neighbor**

# Lạm dụng cụm từ overfitting

Không biết do thói quen hay vì cảm thấy cụm từ này khá **nguy hiểm** mà mình thấy một số bạn mới tìm hiểu về Machine Learning rất thích dùng từ này. Điển hình là việc cứ thấy mô hình dự đoán sai thì nói ngay một câu **Thôi xong. Bị overfitting rồi** hay nói cách khác là cứ mô hình dự đoán kém thì cho là bị **overfitting** khiến cho những người đối diện hết sức hoang mang. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Overfitting.svg/480px-Overfitting.svg.png)

Mình lại xin nhắc lại một chút về khái niệm **Overfitting** trong học máy cho các bạn hiểu để tránh lạm dụng nó. **Overfitting** chỉ hiện tượng mô hình (thuật toán) của chúng ta đạt kết quả rất tốt trên tập dữ liệu huẩn luyện nhưng lại kém trên tập dữ liệu kiểm tra (thực tế). Hiện tượng này có thể ví như một bạn học sinh có tính hay **học vẹt**, tức là chỉ nhớ được những gì mình được dạy chứ không có khả năng suy diễn cho những điều chưa từng học. Song song với **overfitting** là **underfitting** hay là hiện tượng **học dốt** - thuật toán đều đạt kết quả kém trên tập huấn luyện và tập kiểm tra.

Tiện đây mình cũng xin nhắc lại một vài lưu ý về vấn đề này:

* **Thứ nhất:** không phải mô hình nào dự đoán kém cũng bị gọi là **overfitting**, nó còn có thể rơi vào trường hợp thứ hai là **underfitting**
* **Thứ hai:** không phải bất cứ sai sót nào trong quá trình huấn luyện mô hình cũng bị gọi là **overfitting**. Chúng ta không nên lạm dụng cụm từ này một cách tùy tiện

# Không chỉ có một loại performance measures

> **Hỏi:** Làm thế nào để đánh giá được **performance** của một mô hình học máy?
> 
> **Đáp:** Đầu tiên chúng ta cần một tập dữ liệu chia thành hai phần **training** và **testing** sau đó sử dụng một thuật toán học máy học một mô hình từ tập dữ liệu **training**. Tiếp theo sử dụng mô hình đó dự đoán trên tập **testing** và cuối cùng là tìm ra tỉ lệ **số dữ liệu dự đoán đúng / tổng số dữ liệu testing**. Tỷ số này thường được gọi là độ chính xác.

Chắc hẳn không phải lần đầu tiên bạn bắt gặp câu hỏi và câu trả lời như trên. Tất nhiên câu trả lời như phía trên là **không sai** nhưng **chưa đủ**. Rất nhiều người khi nói về độ chính xác của một mô hình học máy thì lầm tưởng rằng chỉ có một cách đo độ chính xác như trên. Trên thực tế cho thấy chỉ số **accuracy** như trên thường được sử dụng để đánh giá hiệu năng của một bài toán phân lớp. Tuy nhiên trong học máy không chỉ có một dạng bài toán là **phân lớp - classification** chính vì thế chũng ta cũng có nhiều hơn các phương pháp để đo đạc độ chính xác của mô hình. Dưới đây mình xin giới thiệu một vài phương pháp phổ biến ứng với từng loại bài toán cụ thể để các bạn tránh bị **nhầm tưởng**.

## Đối với bài toán classification

Đối với dạng bài toán phân lớp chúng ta có thể sử dụng một số phương pháp để đo độ chính xác của mô hình học máy như sau:

### Precision - bao nhiêu cái đúng được lấy ra

Xem xét trên tập dữ liệu kiểm tra xem có bao nhiêu dữ liệu được mô hình dự đoán đúng. Đây chính là chỉ số **accuracy - độ chính xác** như chúng ta sử dụng bên trên. Một cách toán học thì **precision** được biểu diển như sau:

$$Precision=\frac{y_{true} \cap  y_{selected}}{y_{selected}}$$

Tuy nhiên để cho khách quan hơn người ta cần phải xem xét thêm một yếu tố nữa chính là **Recall**

### Recall - bao nhiêu cái được lấy ra là đúng

$$Recall=\frac{y_{true} \cap  y_{selected}}{y_{true}}$$

Chỉ số này còn được gọi là **độ bao phủ** tức là xem xét xem mô hình tìm được có khả năng **tổng quát hóa** như thế nào. Từ hai yếu tố **độ chính xác** và **độ bao phủ** phía trên người ta đưa ra một chỉ số khác gọi là **F1-Score**

### F1-Score

$$F1_-Score=2.\frac{Precision.Recall}{Precision+Recall}$$

Đây được gọi là một **trung bình điều hòa**(harmonic mean) của các tiêu chí Precision và Recall. Nó có xu hướng lấy giá trị gần với giá trị nào nhỏ hơn giữa 2 giá trị **Precision** và **Recall** và đồng thời nó có giá trị lớn nếu cả 2 giá trị **Precision** và **Recall** đều lớn. Chính vì thế **F1-Score** thể hiện được một cách khách quan hơn **performance** của một mô hình học máy.

## Đối với bài toán Regression

Nhắc lại cho các bạn nào chưa rõ, bài toán **regression - hồi quy** tức là biến $y$ của chúng ta không phải là một giá trị rời rạc mà là một giá trị **liên tục**. Nó thường là số lượng, giá tiền, nhiệt độ, lượng mưa ... Do nó là giá trị liên tục nên chúng ta hoàn toàn không thể sử dụng **độ chính xác** để đo **performance** của mô hình được mà cần phải dùng một số loại độ đo khác. Dưới đây mình xin trình bày một vài độ đo cơ bản trong số đó.

### Mean Absolute Error - MAE

**MAE** là một phương pháp đo lường sự khác biệt giữa hai biến liên tục. Giả sử rằng *X* và *Y* là hai biến liên tục thể hiện kết quả dự đoán của mô hình và kết quả thực tế. chúng ta có độ đo **MAE** được tính theo công thức sau:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/3ef87b78a9af65e308cf4aa9acf6f203efbdeded)

Chúng ta có thể cài đặt một đoạn code đơn giản bằng Python sử dụng thư viện Sklearn để tính toán độ đo này như sau:

```
from sklearn.metrics import mean_absolute_error
expected = [0.0, 0.5, 0.0, 0.5, 0.0]
predictions = [0.2, 0.4, 0.1, 0.6, 0.2]
mae = mean_absolute_error(expected, predictions)
print('MAE: %f' % mae)

>>>  MAE: 0.140000
```

Độ đo này thường được sử dụng để đánh giá sự sai khác giữa mô hình dự đoán và tập dữ liệu testing trong các bài toán hồi quy. Chỉ số này càng nhỏ thì mô hình học máy càng chính xác.

### Mean squared error - MSE

**MSE** của một phép ước lượng là trung bình của **bình phương của sai số**, tức là sự khác biệt giữa các giá trị được mô hình dự đoán và gía trị thực. MSE là một **hàm rủi ro**, tương ứng với giá trị kỳ vọng của sự mất mát sai số bình phương hoặc mất mát bậc hai. **MSE** là **moment bậc hai** (về nguồn gốc) của sai số là moment bậc hai (về nguồn gốc) của sai số

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c1abbbe5e9a537dceaf5cbb197fa3cbf387dcf77)

Chúng ta có thể cài đặt chúng trong Python như sau:

```
from sklearn.metrics import mean_squared_error
expected = [0.0, 0.5, 0.0, 0.5, 0.0]
predictions = [0.2, 0.4, 0.1, 0.6, 0.2]
mse = mean_squared_error(expected, predictions)
print('MSE: %f' % mse)
```

# Kết luận

**Machine Learning** là một lĩnh vực mới và khá khó tiếp cận. Tuy nhiên các bạn hãy đi từ những thứ cơ bản nhất và tránh gặp phải những sai lầm trong quá trình học nó. Hi vọng bài viết này một phần nào đó giúp các bạn tránh được những hiểu nhầm đáng tiếc như trên.