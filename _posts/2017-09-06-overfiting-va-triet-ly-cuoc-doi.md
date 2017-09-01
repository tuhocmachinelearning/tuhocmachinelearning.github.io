---
title: "Blog #3 - Overfitting và những triết lý cuộc đời"
last_modified_at: 2017-09-05T16:20:02-05:00
categories:
  - Introduction
tags:
  - Overfiting and life
teaser: 'https://fthmb.tqn.com/4GWkAiQAejmRG1uifK7DsovieS0=/800x0/filters:no_upscale()/about/Illo_Psychology-56f5b0bf5f9b582986653794.png'

excerpt: 'Chào các bạn, chúng ta chào đón nhau bằng một nụ cười thật tươi  và chúc bạn một ngày mới với những niềm vui mới. Các bạn thân mến của tôi, có lẽ rằng với rất nhiều người, khoa học tự nhiên vốn là khoa học của những con số, những công thức, những giải thuật và vô hình chung người ta đã quan niệm rằng nó  tách biệt hoàn toàn với khoa học xã hội - khoa học của các triết lý, khoa học của nhân sinh quan, thế giới quan...'

sidebar:
  nav: "docs"

---
{% include toc %}

Chào các bạn, chúng ta chào đón nhau bằng một nụ cười thật tươi  và chúc bạn một ngày mới với những niềm vui mới. Các bạn thân mến của tôi, có lẽ rằng với rất nhiều người, khoa học tự nhiên vốn là khoa học của những con số, những công thức, những giải thuật và vô hình chung người ta đã quan niệm rằng nó  tách biệt hoàn toàn với khoa học xã hội - khoa học của các triết lý, khoa học của nhân sinh quan, thế giới quan... Chúng  vốn dĩ đã là hai ngành khoa học chẳng thể tách rời nhưng có lẽ vì một lý do nào đó mà rất nhiều người đã không nhìn ra rằng có một sợi dây vô hình song rất bền chặt gắn kết chúng lại với nhau, rằng từ những con số tưởng chừng rất khô khan luôn luôn tiềm tàng một triết lý sống mà đôi khi chúng ta phải mất cả một cuộc đời để trải nghiệm. Điều mà tôi muốn nói đến ngày hôm nay không phải là một vấn đề mới, thậm chí còn là cũ mèm. **Over filting** - một thuật ngữ có lẽ đã quá quen thuộc đối với những người nghiên cứu các giải thuật thống kê và đặc biệt là lĩnh vực **Machine Learning** nhưng ẩn sâu trong nó là những bài học về nhân sinh thật sự kì diệu. Và bạn....chính bạn chứ không phải ai khác, bạn đã sẵn sàng cho con đường tìm ra mối liên hệ rất tự nhiên mà lại kì diệu đó chưa???

![](http://cdn-media-1.lifehack.org/wp-content/files/2014/01/10-Ways-to-Let-Go-of-Past-Relationships.jpg)

## Bạn hiểu thế nào về Over-fitting
Bản chất của **Machine Learning** chính là việc **sử dụng máy tính để mô hình hóa dữ liệu** rồi từ các mô hình đó chúng ta đưa ra các dự đoán cho tương lai. Chúng ta có thể sử dụng rất nhiều các thuật toán khác nhau phục vụ cho việc mô hình hóa dữ liệu của chúng ta, tìm kiếm ra các mối tương quan ẩn chứa trong tập dữ liệu mà chúng ta thu thập được trong quá khứ (chúng ta gọi đó là tập dữ liệu **huấn luyện**). Suy nghĩ của đại đa số người chính là một mô hình **tốt nhất** trên tập dữ liệu huấn luyện thì cũng sẽ tốt nhất khi áp dụng vào thực tế (tức là khi chạy trên tập dữ liệu **kiểm tra**). Điều này đôi khi là một sai lầm, bằng chứng là cho thấy có rất nhiều mô hình cho kết quả rất tốt đối với tập dữ liệu hiện tại nhưng lại hoàn toàn không thể đem áp dụng trên thực tế vì kêt quả dự đoán quá thấp. Hiện tượng mà mô hình dữ liệu **làm việc tốt** trên tập dữ liệu mẫu nhưng lại **bất lực** trước việc dự đoán dữ liệu thực tế được gọi là **Over Fitting** mà theo ngôn ngữ kiếm hiệp người ta gọi là **tẩu hỏa nhập ma**. Chúng ta cùng xem xét một ví dụ như sau:

> **Bài toán dự đoán độ hài lòng của các cặp đôi sau hôn nhân** Bằng các cuộc khảo sát nhiều cặp vợ chồng, các nhà nghiên cứu tâm lý học đã thu được một biểu đồ thể hiện được mức độ hài lòng của các cặp vợ chồng sau khi kết hôn. Chúng ta có thể thấy, nhìn chung thì mức độ hài lòng suy giảm theo thời gian, nhưng mối liên quan với thời gian không hẳn tuân theo phương trình đường thẳng. Trong 3 năm đầu, mức độ suy giảm khá nhanh, nhưng sau đó tăng trong năm thứ 4 và 5; sau 5 năm thành hôn thì mức độ hài lòng lại suy giảm nữa.

![](https://1.bp.blogspot.com/-HfE--7iODUg/WGQ3ex5HxcI/AAAAAAAAEXQ/Kh86bdOp3o0MgiR7-GlBw-GV2xyGky4KgCK4B/s400/Fig%2B1%2Blife%2Bsatisfaction%2Band%2Bdur%2Bmarriage.JPG)

Việc cần làm của những nhà nghiên cứu bây giờ là tìm ra **mô hình** hay **phương trình** tốt nhất để mô tả sự tương quan trong tập dữ liệu đó. Nếu gọi mức độ hài lòng là **y** và thời gian là **t** thì bản chất của chúng ta là đi tìm sự phụ thuộc **y = f(t)**. Dễ thấy được ngay mô hình đơn giản nhất là mô hình **hồi quy tuyến tính**, tức là đi tìm tham số **a** và **b** sao cho **y = a + b.t**. Sử dĩ nó đơn giản vì phương trình chúng ta chỉ phụ thuộc vào duy nhất một tham số **b** liên quan đến thời gian **t** mà thôi.  Mô hình này giải thích được 90% sự khác biệt của dữ liệu như hình dưới (hồi quy tuyến tính là **đường thẳng liền**):
![](https://3.bp.blogspot.com/-NhvFofYxFa8/WGQ3tqLWMfI/AAAAAAAAEXY/SjO_k0zQMZUC0nRambDDz1XSTLiJrFQhgCK4B/s400/Fig%2B2%2Blife%2Bsatisfaction%2Band%2Bdur%2Bmarriage.JPG)

Tuy nhiên chúng ta có thể thấy được rằng mức độ hài lòng có sự biến thiên không tuân theo quy luật tuyến tính, điều này thể hiện ở việc mức độ hài lòng tăng vào năm thứ 4-5 và giảm sau đó. Điều này làm ta nghĩ đến một mô hình có bậc cao hơn. Bằng các kĩ thuật nâng bậc của mô hình với sự trợ giúp của các ngôn ngữ lập trình như **R** hay **Python** chúng ta dễ dàng tìm được mô hình bậc 2 với 2 tham số dạng:

![](https://viblo.asia/uploads/3b5780ab-d82e-4e06-b450-d607c9c834ed.png)

Mô hình này thể hiện bằng **đường nét đứt** như biểu đồ trên. Mô hình này thật sự tốt, nó giải thích được **93%** sự dị biệt của dữ liệu. Tuy nhiên chúng ta vẫn chưa coi thế là đủ, tư tưởng **được đằng chân lân đằng đầu** khiến chúng ta kì vọng có được mô hình tốt hơn giải thích được **100%** phương sai của biến **y**. Việc này cũng chẳng khó khăn với các ngôn ngữ lập trình như **R** chỉ chưa đầy 3 phút chúng ta có thể tìm được một mô hình với 9 tham số, giải thích gần như hoàn toàn sự dị biệt của dữ liệu. Mô hình này thể hiện bằng đường cong in đậm trong hình trên.
**Tuy nhiên**, mục đích của mô hình được tạo ra không phải để giải thích dữ liệu hiện tại, mà để dự đoán được các dữ liệu tương lai sẽ như thế nào.  Vì tương lai là thứ mà chúng ta chưa thể đoán biết được. Vậy câu hỏi đặt ra  là 3 mô hình trên (1 tham số, 2 tham số, và 9 tham số) thì mô hình nào dự báo tốt nhất ???  Không ngạc nhiên khi mô hình 1 tham số tiên lượng mức độ hài lòng tiếp tục giảm trong năm 11, còn mô hình 2 tham số cũng tiên lượng giảm nhưng giảm một chút thôi.  Nhưng điều kì lạ là mô hình 9 tham số tiên lượng rằng năm thứ 11 sau thành hôn thì mức độ hài lòng giảm như là xe hơi lao dốc xuống núi! Đành rằng mức độ hài lòng có thể suy giảm, nhưng không thể nào giảm đột ngột như mô hình 9 tham số dự báo như thế.  Và chúng ta cần phải xem xét lại. Liệu rằng đã có gì đó không đúng chăng???

>**Nghịch lý**: Mô hình giải thích được nhiều dữ liệu trong quá khứ nhất lại là mô hình tiên lượng tồi nhất!

## Người mà bạn chọn lựa làm bạn đời là ai???

Mỗi con người trong chúng ta đều có những tiêu chuẩn riêng để lựa chọn người sẽ đi cùng ta suốt cả cuộc đời. Chúng ta thôi không bàn đến những triết lý của **ngôn tình** như **chỉ cần tình yêu là đủ** ở đây. Tình yêu là chuyện của con tim, còn tiêu chuẩn để lựa chọn là chuyện của lý trí. Một người thiếu trái tim - người đó chết. Một người mất đi lý trí - người đó chẳng thể sống được. Vậy nên đứng trước những sự lựa chọn lớn lao của cuộc đời, chúng ta cần tuân thủ rất nhiều nguyên tắc, rất nhiều tiêu chuẩn. Tuy nhiên, thực tế lại chứng minh rằng chúng ta đừng lựa chọn quá nhiều, đừng áp đặt lên người khác quá nhiều tiêu chuẩn. **Over fitting** thể hiện trong việc chọn lựa bạn đời là việc chúng ta cố gắng áp đặt quá nhiều tiêu chuẩn cho người bạn đời của chúng ta nhưng lại quên mất rằng, tất cả những tiêu chuẩn đó chỉ được xem xét trong quá khứ và hiện tại, mà biểu hiện của con người đó ở tương lai như thế nào không ai có thể biết trước được. Và bạn có muốn người bạn đời của mình giống như một mô hình dữ liệu,  dù rất tốt khi xem xét ở hiện tại nhưng hoàn toàn bất lực với những thay đổi ở tương lai không. Vậy nên:
> **Không có tiêu chuẩn để lựa chọn -  bạn đang đánh cược với tương lai. Có quá nhiều tiêu chuẩn để lựa chọn - chính tương lai đang đánh cược với bạn**

![](http://img.v3.news.zdn.vn/w660/Uploaded/nphpayp/2014_06_17/18614_su_tu.jpg)

## Quá khứ chỉ là kỉ niệm. Đừng sống mãi trong chiếc bong bóng của riêng mình
Vấn đề của **Over fitting** không hẳn chỉ là một vấn đề trong ngành khoa học máy tính. Đôi khi chúng ta thấy thật sự nó rất đời thường, rất nhân sinh. Có lẽ không ít người trong mỗi  chúng ta đang ở trong một chiếc bong bóng vô hình mà không hay biết. Không ít người trong số chúng ta thường có xu hướng nói nhiều về quá khứ hơn là nhắc đến tương lai. Có rất nhiều người thích lặp đi lặp lại những chuyện **Xưa rồi Diễm**, rằng ngày xưa tôi đã từng rất giỏi, ngày xưa tôi đã từng rất hạnh phúc, ngày xưa tôi đã.....**Stop**. Chúng ta là những con người đang sống ở hiện tại và tương lai là những điều chưa ai có thể biết trước. Đừng mải mê trong quá khứ vàng son và cũng đừng bi lụy vì một quá khứ lầm lỗi. Dù bạn là ai, bạn có quyền được quyết định chính tương lai của bạn và thay đổi để sống tốt hơn, sống đẹp hơn chưa bao giờ là muộn cả. Và nếu như ranh giới giữa những hạnh phúc hay khổ đau của quá khứ với những điều kì diệu của tương lai cũng mong manh như một bong bóng xà phòng, thị bạn đã sẵn sàng thoát ra khỏi chiếc bong bóng của mình đễ ngắm nhìn một thế giới tốt đẹp hơn chưa???

![](http://cdn.tinybuddha.com/wp-content/uploads/2011/03/Let-Go.jpg)

## Đừng quá cầu toàn. Mọi thứ có thể thay đổi và quan trọng là biết thích nghi
Bạn có tin là có những thứ đến Google cũng không có câu trả lời cho bạn không??? Đúng là như vậy đấy, tôi đang nói riêng về phương diện tìm kiếm tri thức thôi, chúng ta dã là quá nhỏ bé rồi. Đến cả Google cũng không thể nói rằng biết hết **100%** về mọi lĩnh vực thì huống gì chúng ta. Tôi biết có rất nhiều người rất cầu toàn, sự cầu toàn không phải là một cái gì đó sai trái, nó giúp cho con người ta biết chu toàn bổn phận và trách nhiệm của bản thân mình một cách nghiêm khắc hơn. Tuy nhiên, sự cầu toàn thái quá dễ dẫn con người ta đến cảm giác tiêu cực, cảm giác bị thất bại khi có một mục tiểu không hoàn thành. Có một điều bạn phải chấp nhận rằng:
>**Chúng ta không bao giờ có thể là người hoàn hảo**

Có lẽ bạn thấy một con người rất giỏi về lập trình phần mềm và bạn ngưỡng mộ người đó vì đó là chuyên môn của bạn, nhưng chính bản thân người đó lại rất yếu kém ở một mảng khác ngoài chuyên môn ví dụ như nấu ăn chẳng hạn. Cuộc sống luôn cần những khoảng trống để lấp đầy, nếu một ai đó mà chẳng có một khoảng trống nào để lấp đầy thì họ thật cô đơn biết bao???

![](http://outofcomfort.weebly.com/uploads/5/4/7/5/54755535/466328_orig.jpg)

## Đừng thần tượng hóa ai cả. Hi vọng càng nhiều thì thất vọng càng lớn

Tôi biết có rất nhiều người thực sự rất đáng để chúng ta ngưỡng mộ, có rất nhiều người thực sự rất có khả năng trong một lĩnh vực nào đó và họ xứng đáng được xã hội công nhận. Tuy nhiên có rất nhiều người mắc một căn bệnh mà giới trẻ bây giờ gọi là bênh **Fan cuồng**. Tôi còn nhớ một câu chuyện kể rằng khi **Bi Rain**  - một diễn viên, một ca sĩ nổi tiếng của Hàn Quốc - trong một lần sang lưu diễn tại Việt Nam đã thu hút rất nhiều Fan hâm mộ trẻ đến cổ vũ. Việc đó thì cũng chẳng có gì là lạ cho đến một ngày người ta đưa lên mạng một đoạn video khi **Bi Rain** rời đi thì một đám đông các Fan cuồng chạy lên chiếc ghế mà anh ta ngồi thi nhau **hít hà** chiếc ghế đó như thể hít một thứ sinh khí từ trời ban xuống vậy. Thật là ngô nghê buồn cười, sự thần tượng hóa một ai đó giống như việc chúng ta đang cố gắng tập trung một cách thái quá vào dữ liệu mà chúng ta thu thập được mà quên đi mất bản chất của vấn đề. Thậm chí chính sự thần tượng hóa đó lại gây ra những hệ lụy vô cùng to lớn khi chúng ta biết được sự thật rằng trên thực tế có thể thần tượng của ta không được như chúng ta mong đợi. **Thần tượng hóa** là một thể hiện của **Over fitting** trong đời sống con người, nó có thể làm con người ta lạc quan hơn, nhưng cũng có thể làm cho người ta thất vọng hơn khi quay về với thực tại. Vậy nên, tốt nhất là **Đừng thần tượng hóa ai cả**

![](http://slodive.org/wp-content/uploads/2013/04/quotes-about-being-hurt/hope-too-much.jpg)

## Và cuối cùng. Hãy học cách sống trung dung
Tôi biết rằng khi đứng trước một vấn đề của cuộc sống, có rất nhiều người hay có thói quen suy nghĩ rất nhiều, đôi khi là phức tạp hóa vấn đề đến mức tối đa. Tuy nhiên suy nghĩ nhiều quá có thể giúp chúng ta giải thích được những gì mình quan sát trong quá khứ (và hiện tại), nhưng nó không hẳn giúp ích chúng ta trong quyết định cho tương lai mà có thể làm cho tình hình rối lên. Trái ngược lại có những người chẳng suy nghĩ, hoặc suy nghĩ rất ít trước một vấn đề. Thái độ **mặc đời trôi** của những người như vậy cũng không cho chúng ta một cách giải quyết hiệu quả cho tương lai. Hiện tượng đó tương tự như **under-fitting** trong khoa học dữ liệu, nó bỏ sót và tiên lượng kém chính xác. Thành ra, nghệ thuật của mô hình hoá các mối liên quan là tìm một mô hình không có quá nhiều tham số mà cũng không có quá ít tham số. Nghệ thuật này cũng là nghệ thuật sống: **tìm cách sống trung dung.**. Hãy sống ôn hòa, bình thản trước mọi vấn đề của cuộc sống, không tầm thường hóa nhưng cũng không cường điều hóa vấn đè. 

>*Cần phải giữ cho ý nghĩ và việc làm luôn luôn ở mức trung hòa, không thái quá, không bất cập và phải cố gắng ở đời theo nhân, nghĩa, lễ, trí, tín, cho thành người quân tử* - **Sách Trung Dung - Tử Tư**

![](http://www.fineyaculacionprecoz.com/wp-content/uploads/2015/11/Meditating-in-lotus-position-via-Shutterstock.jpg)

## Lời kết
Từ một vấn đề tưởng chừng đã quá quen thuộc như **Over fitting** vẫn luôn tiềm ẩn trong nó những triết lý nhân sinh mà chúng ta đáng học hỏi mà cuối cùng tựu chung lại đó là cách sống trung dung trước mọi vấn đề xảy ra trong cuộc đời. Đứng trước những sự việc xảy ra bạn sẽ chọn cách nhìn nhận nó như thế nào. **Và đứng trước cả vũ trụ rộng lớn - bạn sẽ chọn bạn là ai???**

