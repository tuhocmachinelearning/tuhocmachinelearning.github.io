---
title: "Blog #2 - Lý thuyết xác suất cơ bản sử dụng trong Machine Learning"
last_modified_at: 2017-08-22T16:20:46-05:00
categories:
  - Theory
tags:
  - Probability
  - Random Variable
  - Probability Distributions
  - Expectation and Variance
  - Bayes Rule
teaser: 'https://www.statphys.sissa.it/dices_new.jpg'
excerpt: 'Có thê nói một điều rằng lý thuyết xác suất là một trong những lý thuyết quan trọng nhất của khoa học hiện đại và đặc biết là Machine Learning bởi vì đa phần các thuật toán của Machine Learning đều có cơ sở dựa trên xác suất. Trong bài viết này tôi sẽ tổng hợp lại những kiến thức xác suất cơ bản đó giúp cho các bạn ôn tập lại kiến thức của mình nhằm tiếp cận Machine Learning một cách dễ dàng hơn.'

sidebar:
  nav: "docs"

---
{% include toc %}
# Giới thiệu
Có thê nói một điều rằng **lý thuyết xác suất** là một trong những lý thuyết quan trọng nhất của khoa học hiện đại và đặc biệt là **Machine Learning** bởi vì đa phần các thuật toán của **Machine Learning** đều có cơ sở dựa trên xác suất. Nếu như bạn là một người mới bắt đầu bước chân vào lĩnh vực **học máy** bạn có lẽ sẽ tiếp cận với những **Tutorial** trên mạng theo hướng đi ăn xổi ở thì. Bạn có thể làm được một vài điều khá là hay ho, khá là kì diệu đối với bạn ở thời điểm đó như nhận diện được đâu là một chú mèo trong bức ảnh, dự đoán được biến động của thị trường chứng khoán ngày mai là như thế nào, chuẩn đoán được một người có phải bị bệnh HIV hay không... Tất nhiên những thứ đó giúp cho bạn có thứ cảm giác rất sung sướng khi làm được một điều gì đó với lĩnh vực mới này. Tuy nhiên khi bạn càng tìm hiểu sâu về nó thì bạn sẽ thấy có những vấn đề không thể có một **Tutorial** nào cho bạn cả, bản thân bạn phải tự giải quyết nó. Đến lúc đó bạn sẽ lại phải vòng ngược lại và tự vấn bản thân rằng **vì sao người ta lại sử dụng thuật toán này để giải quyết bài toán đó???**. Và đây chính là lúc bạn tìm về với **lý thuyết xác suất** một trong những lý thuyết cơ sở để hình thành nên nhưng thuật toán của **Machine Learning**. Trong bài viết này tôi sẽ tổng hợp lại những kiến thức xác suất cơ bản đó giúp cho các bạn ôn tập lại kiến thức của mình nhằm tiếp cận **Machine Learning** một cách dễ dàng hơn.

# Không gian xác suất


Chúng ta đã được học đến khái niệm về xác suất trong bất kì chương trình đại học về kĩ thuật hoặc kinh tế nào. Khi nói đến **xác suất** là người ta nói đến các **lý thuyết toán học** về sự **bất định - uncertainly** hay nói một cách khác, **xác suất** biểu thị khả năng xảy ra của các sự kiện - *event* trong một môi trường bất định  nào đó.  Ví dụ chúng ta xét về xác suất có mưa hay không có mưa vào thứ hai tuần tới, xác suất tỏ tình thành công hay thất bại của cậu bạn thân... Tóm lại cứ nói đến xác suất là đề cập đến sự **không chắc chắn** hay **bất định** đó.

Về mặt toán học, người ta kí hiệu một **không gian xác suất - probability space** bao gồm 3 thành phần $$(\Omega , F, P)$$  như sau:
* $$\Omega$$ chính là tập các giá trị có thể xảy ra - **possible outcome** với sự kiện trong không gian xác suất. Người ta còn gọi nó là **không gian mẫu**
* $$F \subseteq  2^{\Omega}$$ - (cái này là lũy thừa cơ số 2 của $$\Omega$$) là tập hợp các sự kiện có thể xảy ra trong không gian xác suất
* $$P$$ là xác suất (hoặc **phân phối xác suất**) của sự kiện. $$P$$ ánh xạ một sự kiện $$E \in F$$ vào trong một giá trị thực $$p \in \left [ 0;1 \right ]$$. Ở đây chúng ta gọi $$p = P(E)$$ là xác suất của sự kiện $$E$$

## Ví dụ minh họa
Chúng ta cùng nhau xem xét một ví dụ khá kinh điển trong lý thuyết xác suất đó chính là **ví dụ tung xúc sắc**

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWD6A5kOwmAxizSUyWJX60UYNxKqrgBMyqIb94NSoaF6Bl_uH-Pg)

Giả sử rằng chúng ta tung một con xúc sắc 6 mặt. Không gian các **outcomes** có thể xảy ra trong trường hợp này là $$\Omega = \left \{ 1, 2, 3, 4, 5, 6 \right \}$$ - chúng ta không tính đến các trường hợp xúc sắc rơi lơ lửng tức là không thuộc mặt nào. Không gian các sự kiện $$F$$ sẽ tùy thuộc vào sự định nghĩa của chúng ta. Ví dụ chúng ta định nghĩa **sự kiện xúc sắc là mặt chẵn hoặc mặt lẻ** thì không gian sự kiện $$F=\left \{ \varnothing  ,  \left \{ 1, 3, 5 \right \}, \left \{ 2, 4, 6 \right \}, \Omega \right \}$$ trong đó $$\varnothing $$ là sự kiện có xác suất 0 - hay còn gọi là **biến cố không thể có**. $$\Omega$$ là sự kiện có xác suất 1 - hay còn gọi là **biến cố chắc chắn**

## Các tính chất của xác suất
Giống như ví dụ ở phía trên, khi không gian mẫu - **outcomes space** là hữu hạn thì chúng ta thường lựa chọn không gian sự kiện $$F=2^{\Omega} = \left \{ \varnothing  ,  \left \{ 1, 3, 5 \right \}, \left \{ 2, 4, 6 \right \}, \Omega \right \}$$. Cách tiếp cận này chưa hẳn đã tổng quát hóa cho mọi trường hợp tuy nhiên nó **đủ dùng** trong các bài toán thực tế, tất nhiên là với giả thiết không gian mẫu của chúng ta là **hữu hạn**. Khi không gian mẫu là **vô hạn - infinite** chúng ta phải hết sức cẩn thận trong việc lựa chọn không gian sự kiện $$F$$.  Khi đã định nghĩa dược không gian sự kiện $$F$$ thị hàm xác suất của chúng ta **bắt buộc** phải thỏa mãn các tính chất sau đây:
* **Không âm - non-negativity** - xác suất của mọi sự kiện là không âm, tức là với mọi $$x \in F,~~ P(x)\geq 0$$
* **Xác suất toàn cục - trivial event**  $$P(\Omega) = 1$$
* **Tính cộng - additivity** tức là với mọi $$x, y \in F$$ nếu như $$x\cap y= \varnothing$$ thì ta có $$P(x\cup y) = P(x) + P(y)$$

# Biến ngẫu nhiên - Random Variables

***Random Variables*** là một thành phần quan trọng trong lý thuyết xác suất. Nó biểu diễn giá trị của các đại lượng không xác định, thông thường nó được coi như một **ánh xạ** từ tập các **outcomes** trong không gian mẫu thành các giá trị thực.

![](http://archive.cnx.org/resources/64fd28e79e27bc8f4d43303ca7d6a27ba13d7f9e/Figure2-1.png)

Quay trở lại với ví dụ tung xúc sắc phía trên, gọi $X$ là biến ngẫu nhiên biểu diễn kết quả của các những lần gieo xúc sắc. Một lựa chọn khá tự nhiên và đơn giản đó là:

> $$X$$ là số chấm tròn trên mặt tung được

Chúng ta cũng có thể lựa chọn một chiến lược biểu diễn biến ngẫu nhiên $$X$$ khác chẳng hạn như sau:

$$
X = \begin{cases}
 & 1 \text{ if i is odd} \\
 & 0 \text{ if i is even}
\end{cases} ~~(1)
$$


Có nghĩa là cùng một biến cố nhưng biểu diễn nó như thế nào là việc của mỗi chúng ta. Biến ngẫu nhiên $X$ biểu diễn như biểu thức $(1)$ được gọi là **binary random variables** - biến nhị phân. *Biến nhị phân* được sử dụng rất thông dụng trong thực tế công việc nhất là *Machine Learning* và thường được biết đến với cái tên **indicator variables** nó thể hiện sự xảy ra hay không xảy ra của một **sự kiện**

Từ nay trở đi, chúng ta sẽ nói về xác suất đối với các biến ngẫu nhiên.  Nếu các bạn đọc ở một số tài liệu về xác suất thì có thể thấy một số kí hiệu của chúng như sau:

$$P(X=a)~~or~~P_X(a)~~(2)$$

Công thức $(2)$ biểu diễn xác suất của một biến ngẫu nhiên $X$ tại giá trị $a$. Ngoài ra người ta còn kí hiệu khoảng giá trị của một biến ngẫu nhiên $X$ là $Val(X)$

## Biến rời rạc và biến liên tục

Có hai loại biến ngẫu nhiên đó là **BNN rời rạc** và **BNN liên tục**. **Rời rạc** có thể hiểu một cách đơn giản là giá trị của nó thuộc vào một tập định trước. Trong **Machine Learning** các giá trị này tương ứng với các phân lớp (*class*).  Ví dụ tung xúc sắc bên trên là một điển hình của **biến ngẫu nhiên rời rạc** và hàm xác suất của nó được định nghĩa như sau:

$$\sum_{\forall x}{p(x)}=1~~(3)$$

Còn biến ngẫu nhiên liên tục có thể định nghĩa là các biến ngẫu nhiên mà các giá trị của nó rơi vào một tập **không biết trước**. Trong **Machine Learning** người ta gọi lớp bài toán với **biến ngẫu nhiên liên tục** là **Hồi quy**. Giá trị của nó có thể nằm trong một **khoảng hữu hạn** ví dụ như thời gian làm bài thi đại học là $t \in \left ( 0;180 \right )$ phút hoặc cũng có thể là **vô hạn** ví dụ như thời gian từ bây giờ đến ngày tận thế $t \in \left ( 0; +\infty \right ) $ chẳng hạn. Khi đó hàm mật độ xác suất của nó trên toàn miền giá trị $D$ của **outcomes space** được định nghĩa bằng một tích phân như sau:

$$\int_{D}p(x)dx=1~~(4)$$

> **Note**: nếu $x$ là **BNN liên tục** thì $p(x)$ có thể là một số dương bất kì miễn sao nó đảm bảo được công thức $(4)$


# Phân phối của biến ngẫu nhiên

Tôi sẽ quay trở lại với ví dụ trong phần [Không gian xác suất](/theory/probability-for-machine-learning/#ví-dụ-minh-họa) đã thảo luận phía trên. Tại ví dụ này chúng ta giả sử không gian sự kiện $F=2^{\Omega}$ từ đó chúng ta định nghĩa xác suất $P$ thông qua $F$ như sau:

$$P(\left \{ 1 \right \}) = P(\left \{ 2 \right \}) = ... = P(\left \{ 6 \right \}) = 1/6$$

Và giả sử rằng việc tung xúc sắc ra các mặt là hoàn toàn **độc lập** - tức là việc ra mặt nào **không phụ thuộc** vào các lần gieo xúc sắc trước đó thì chúng ta có được theo công thức cộng xác suất ta có xác suất của sự kiện **xúc sắc ra mặt chẵn** là:

$$P(\left \{ 2, 4, 6 \right \}) = P(\left \{ 2 \right \}) + P(\left \{ 4 \right \}) + P(\left \{ 6 \right \})$$

$$ = 1/6 + 1/6 + 1/6 = 1/2$$
