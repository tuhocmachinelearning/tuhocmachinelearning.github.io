---
title: "Blog #7 - [Data Analysis] Phân tích dữ liệu xổ số miền Bắc"
last_modified_at: 2017-10-06T16:20:02-05:00
categories:
  - Data_Analysis
tags:
  - Data_Analysis
teaser: 'http://cms.xosovietnam.vn/files/xo-so_bepvh.jpg'

excerpt: 'Có lẽ từ xổ số hay lottery đã không còn là cụm từ xa lạ đổi với mỗi người chúng ta. Thậm chí dân chơi còn có một câu khá nổi tiếng ví von như sau:

Lô đề cờ bạc muôn đời thịnh Học hành chăm chỉ vạn kiếp suy

Nghe mà muốn khóc quá chừng, mình làm Đa ta sai ừn vất vả là thế mà vẫn vạn kiếp suy thì tính sao bây giờ. Trong một phút yếu lòng mình đã nghĩ đến việc thử phân tích dữ liệu xổ số miền Bắc từ một trang mạng để xem câu tục ngữ trên có thực sự có hiệu quả không. OK không để mất thời gian của các bạn chúng ta sẽ bắt đầu ngay với một lĩnh vực mới trong khai phá dữ liệu đó chính là tính lô đề. Let go....'

sidebar:
  nav: "docs"

---
{% include toc %}

Có lẽ từ **xổ số** hay **lottery** đã không còn là cụm từ xa lạ đổi với mỗi người chúng ta. Thậm chí dân chơi còn có một câu khá nổi tiếng ví von như sau:

> **Lô đề cờ bạc muôn đời thịnh**
> **Học hành chăm chỉ vạn kiếp suy**

Nghe mà muốn khóc quá chừng, mình làm **Đa ta sai ừn** vất vả là thế mà vẫn **vạn kiếp suy** thì tính sao bây giờ. Trong một phút yếu lòng mình đã nghĩ đến việc thử phân tích dữ liệu **xổ số miền Bắc** từ một trang mạng để xem câu **tục ngữ** trên có thực sự có hiệu quả không. OK không để mất thời gian của các bạn chúng ta sẽ bắt đầu ngay với một lĩnh vực mới trong **khai phá dữ liệu** đó chính là **tính lô đề**. Let go....


# Cơ sở lý thuyết

Nói qua một chút cho các bạn nào chưa hiểu về luật chơi xổ số hay nói chính xác hơn là **chơi đề** áp dụng trên toàn **vịnh Bắc Bộ**. Kết quả **đề** của một hôm được tính bằng hai chữ số cuối của giải đặc biệt. Và nếu người chơi đánh trúng thì giải thưởng sẽ là **1 ăn 70**. Chỉ một luật chơi đơn giản như vậy mà làm cho rất nhiều người say mê đó các bạn ạ. Mình thì không thích những thứ thuộc về may mắn lắm, nói đúng hơn mình thích những thứ gì có thể tính toán được, có bằng chứng khoa học cụ thể. Chính vì lý do đó nên từ trước đến giờ mình không mấy quan tâm đến việc **chơi xổ số** (thực ra hồi bé có chơi một lần nhưng bị thua nên không bao giờ chơi nữa :slight_smile:) nhưng tình cờ đọc được một bài viết chia sẻ trên mạng về cách tính toán soi lô đề nên với cái máu của một người thích các con số mình đã quyết định tải thử tập dữ liệu về và phân tích thử. Các bạn có thể tải về tập dữ liệu này tại [đây](https://sodepmb.com/so-ket-qua-xo-so-mien-bac-tu-2002-2017.html). Thống kê đầy đủ và chi tiết từ năm **2002** đến năm **2017**. Sau khi có dữ liệu rồi chúng ta sẽ tiến hành xử lý chúng nhé


![](http://cms.xosovietnam.vn/files/xo-so_bepvh.jpg)


# Chuẩn bị dữ liệu

Dữ liệu được tải về dưới dạng file **.docx** được lưu thành từng bảng cho từng năm. Các bạn cứ tải hết về theo các link đã cung cấp sẽ thu được một tập dữ liệu như sau:

![](https://viblo.asia/uploads/75f5d065-60ec-415b-b2bf-a822db3e901c.png)

Mở thử một file ra thì sẽ thấy mỗi file sẽ được lưu theo một bảng gồm các cột tương ứng với 12 tháng trong một năm, và các dồng tương ứng với các ngày trong một tháng

![](https://viblo.asia/uploads/ab2a5891-84fe-4b50-a4b9-3a15c0d4778c.png)

Tuy nhiên để thuận tiện cho việc lập trình lấy dữ liệu sau này chúng ta sẽ cần tổng hợp lại dữ liệu này để lưu dưới dạng file **xls** hoặc **csv** chẳng hạn. Rất đơn giản chúng ta chỉ cần copy lần lượt các bảng tại từng file vào trong một editor như [Google Trang tính](https://www.google.com/intl/vi_VN/sheets/about/) chẳng hạn. Sau đó chúng ta lưu về thành một file tại local để tiện cho xử lý về sau. Nếu các bạn lười thu thập có thể dùng sẵn file mà mình đã làm [tại đây](https://github.com/thandongtb/loto/blob/master/loto.xls). OK vậy là đã xong bước chuẩn bị dữ liệu giờ chúng ta sẽ tiếp tục sang bước tiếp theo đó là **Tiền xử lý dữ liệu**


# Tiền xử lý dữ liệu

Sau khi đã thu thập được file dữ liệu rồi chúng ta sẽ tiến hành xử lý chúng. Quan sát một lát thấy file dữ liệu của chúng ta được lưu dưới dạng bảng và chúng ta sẽ sử dụng một công cụ nào đó để chuyển chúng về dạng **array** có thể xử lý được. Chúng ta sẽ sử dụng một thư viện nổi tiếng trong `Python` đó chính là `pandas`. Nó chuyên dùng cho việc xử lý các dữ liệu thuộc dạng bảng. Một thư viện khác để xử lý dữ liệu số rất nổi tiếng trong ``Python`` đó chính là ``Numpy`` Chúng ta tiến hành import các thư viện này vào như sau:

```
import pandas as pd
import numpy as np
```

Tiếp theo chúng ta sẽ load dữ liệu ra bằng lệnh sau:

```
file = 'loto.xls'
df = pd.read_excel(file)
```

Dữ liệu được sinh ra dưới dạng ``DataFrame`` như sau:

![](https://viblo.asia/uploads/c8694a01-4faf-40f2-bee4-afcc1a474c50.png)

Quan sát thấy thư viện pandas đang sử dụng bằng số thực. Chúng ta cần chuyển nó về thành số nguyên

```
df_matrix = df.as_matrix()
df_matrix = np.int_(df_matrix)
print df_matrix[-1]
```

Sau khi tiến hành in thử dòng cuối cùng của file dữ liệu thì chúng ta nhận được kết quả như sau:

![](https://viblo.asia/uploads/99c90206-5ea4-4cce-a3d8-95a60bd860be.png)

## Loại bỏ missing value

Giá trị ``-9223372036854775808`` tương ứng với những giá trị ``NaN`` sau khi convert sang ``numpy`` điều này chứng tỏ rằng dữ liệu chúng ta đang bị thiếu hay trong **Data Science** gọi đó là các **missing value** chúng ta có một số cách xử lý chúng như sau:

* Lấy giá trị trung bình của các giá trị còn lại thay vào **missing value**
* Gán **missing value = 0** 
* Sử dụng phương pháp ``kNN - k Nearest Neighbor`` tính toán giá trị của missing value
* Bỏ qua missing value trong tập dữ liệu


Tuy nhiên đối với dữ liệu của chúng ta là **kết quả xổ số** là các giá trị thực tế đòi hỏi tính chính xác tuyệt đối nên cách tốt nhất chính là bỏ qua không cần xử lý các giá trị bị thiếu. Chúng ta quan sát thấy các giá trị bị thiếu tương ứng với các giá trị  ``-9223372036854775808`` hay trong trường hợp này là các giá trị âm - vì kết quả xổ số là một số không âm. Nên chúng ta sẽ dùng một hàm bỏ qua các giá trị thiếu đồng thời xử lý các giá trị xổ số bằng cách lấy 2 chữ số cuổi cùng của giải đặc biệt - chính là **số đề** như sau:


```
def checker(d_arr):
    tmp = []
    for i in d_arr:
        if i < 0:
            tmp.append(i)
        else:
            tmp.append(i % 100)
    return tmp
```

Và cuối cùng hàm load dữ liệu của chúng ta sẽ như sau:

```
def read_data():
    file = 'loto.xls'
    df = pd.read_excel(file)
    df_matrix = df.as_matrix()
    df_matrix = np.int_(df_matrix)
    df_matrix = [checker(d) for d in df_matrix]
    return np.array(df_matrix)
```

##  Trích xuất dòng và cột
Quan sát dữ liệu của chúng ta cho thấy các hàng sẽ biểu diễn tương ứng với các ngày trong một năm, các cột sẽ biểu diễn tương ứng với các tháng trong một năm. Chúng ta sẽ viết hai hàm để đọc dữ liệu dạng này

```
def get_rows(data, s_row = 0, e_row = 1):
    return data[s_row:e_row]

def get_columns(data, s_col = 0, e_col = 12):
    cols = [np.array(d)[s_col:e_col] for d in data]
    cols = data_concate(cols)
    return cols
```

Ví dụ như lấy dữ liệu của năm đầu tiên sẽ tương ứng với 31 dòng và 12 cột dữ liệu đầu tiên. Chúng ta thực hiện như sau:

```
data = read_data()
print get_rows(data, 0, 31)
```

![](https://viblo.asia/uploads/123aace5-ea13-4415-b70b-b84a69ed0fc4.png)

Chúng ta thấy rằng dữ liệu của chúng ta đang chứa hai chữ số cuối và những giá trị âm tương ứng với các **missing value** được lưu theo dạng ``2d array`` chúng ta cần chuyển chúng về dạng ``1d array`` và loại bỏ những số âm này đi trước khi xử lý

```
def data_concate(data):
    concate = np.concatenate(data)
    concate = np.array([num for num in concate if num >= 0])
    return concate
```

Quay về hàm main chúng ta thay đổi một chút để thấy kết quả

```
print data_concate(get_rows(data, 0, 31))
```

![](https://viblo.asia/uploads/7ca73618-fe90-4613-aff9-fcd354da5698.png)

Và đây chính là toàn bộ các con đề trong năm đầu tiên tức năm 2002. Chúng ta sẽ thử vẽ đồ thị biểu diễn phân phối của các con số này xem sao nhé.

# Biểu diễn dữ liệu bằng đồ thị

Chúng ta sẽ biểu diễn dữ liệu bằng đồ thị với hàm sau:

```
def plot_data(data):
    counter = Counter(data)
    labels, values = zip(*counter.items())
    indexes = np.arange(len(labels))
    width = 0.5
    plt.xlabel('Numbers')
    plt.ylabel('Frequence')
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()
```

Với dữ liệu của năm đầu tiên chúng ta hay thử quan sát nhé

![](https://viblo.asia/uploads/c698a3e6-9798-4564-8f40-9f2ccc3975a7.png)

## Nhận xét

> Những số đề phần đa xuất hiện khoảng 2 đến 4 lần trong một năm. Cá biệt có những số xuất hiện chỉ một lần hoặc 8 hay 9 lần những rất ít khi xảy ra. 

Kể ra thì cũng đúng với lý thuyết xác suất. Nếu chúng ta coi việc  quay giải xổ số giống như việc chúng ta đang ném ngẫu nhiên **365** hòn đá (tương ứng với 365 ngày trong năm) vào **100** cái nhà tương ứng với các số từ 0 đến 99 thì trung bình chúng ta sẽ có được giá trị của kì vọng như sau:

$$E(X)=\frac{m}{n}=\frac{365}{100}=3.65$$

Trông thì có vẻ ngẫu nhiên đấy nhưng nhỡ đâu có quy luật gì đó trong đây thì sao. Thử đào tiếp một chút nữa xem sao nhé các bạn, biết đâu làm tìm thêm được một phương pháp tính lô mới.


# Tính toán hàm mục tiêu

Hãy tưởng tượng rằng việc đánh xổ số của ta giống như một bài toán **tối ưu** tức là làm tăng tối đa giá trị của hàm mục tiêu ở đây tức là tăng tối đa phần thưởng bằng một số phương pháp nào đó. Như đã đưa ra luật chơi ở phần đầu. Chúng ta sẽ xây dựng hàm mục tiêu như sau:


```
def loto_lost_func(loto_arr, rs = 0, price = 0):
    total = - price * len(loto_arr)
    if rs in loto_arr:
        total = total + price * 70
    return total
```

Hàm trên nhận đầu vào gồm các tham số sau:

* ``loto_arr`` là bảng chứa các con đề bạn đánh trong ngày cần tính
* ``rs`` là kết quả xổ số (hai chữ số cuổi) của ngày cần tính
* ``price`` là số tiền bỏ ra cho mỗi con đề.


Hãy chạy thử hàm trên 

```
print loto_lost_func(loto_arr=[12, 32, 44, 55], rs=22, price=20000)

>>> -80000
```

trong trường hợp này ``rs`` không trùng với bất kì số nào trong ``loto_arr`` tức hôm đó bạn không trúng đề và tổng số tiền bạn thu lại là ``-80000``. Nếu trong trường hợp này bạn trúng và kết quả của bạn sẽ khác

```
print loto_lost_func(loto_arr=[12, 32, 44, 55], rs=12, price=20000)

>>> 1320000
```

Trường hợp này bạn đã được lãi ``1320000`` do trúng số đề **12**. Khá là thú vị phải không. Nhưng một vấn đề là làm cách nào để có thể tìm ra được ``loto_arr`` tức là các số cần đánh trong ngày hôm nay để có thể có xác suất trúng cao nhất. Chúng ta hãy cùng nhau xem xét tiếp các trường hợp sau

# Chơi xổ số kiểu gà mờ
Việc cần làm của chúng ta đó là lựa chọn ra được danh sách các con số có thể đem đánh trong một ngày. Tuy nhiên rằng để cho khách quan chúng ta sẽ xét xem nếu áp dụng cùng một cách chơi cho tất cả các ngày trong năm thì chúng ta sẽ được lãi bao nhiều nhé. Đầu tiên đó là lựa chọn ngẫu nhiên

## Lựa chọn ngẫu nhiên 5 số

Giả sử bạn lấy ngày sinh của bố mẹ, em gái, em trai và bạn tạo thành một bố số như sau ``loto_arr = [18, 5, 27, 6, 28]`` sau đó áp dụng bộ số này cho cả năm 2002 thử xem sao nhé. Trước tiên là load dữ liệu của năm 2002 tương ứng với năm đầu tiên của tập dữ liệu. Hàm load dữ liệu cho từng năm như sau:

```
def get_data_range(s_year, e_year):
    data = read_data()
    data = get_rows(data, s_year * 31 + 1, e_year * 31 - 1)
    return data_concate(data)

# Load data for 2002
data_2002 = get_data_range(0, 1)
```

Sau đó chúng ta sẽ tính toán tổng số tiền sẽ đạt được trong năm 2002 nếu như áp dụng bộ số ngẫu nhiên ngày sinh của chúng ta. Hàm tính toán đó như sau

```
def total_lost(test_data, loto_arr = None, price = 0):
    total = 0
    for rs in test_data:
        lost = loto_lost_func(loto_arr, rs=rs, price=price)
        total += lost
    return total
    
loto_arr = [18, 5, 27, 6, 28]
print total_lost(test_data=data_2002, loto_arr=loto_arr, price=20000)

>>> -9800000
```

Ồ kết quả là số âm, có vẻ không ổn lắm bởi có lần thua có lần được nếu cứ đánh hết 5 con tương đương **100000 VNĐ** một ngày thì một năm chúng ta sẽ bị lỗ mất **gần 10 triệu**. Thật là một con số không ổn cho việc đánh ngẫu nhiên. Giờ thử cách khác xem sao

## Lựa chọn ngẫu nhiên nhiều số

Khả năng 5 số thì xác suất trung hơi thấp nên chúng ta chấp nhận thương đau quất luôn 20 số một ngày cho chắc cú với hi vọng sẽ được nhiều tiền thưởng hơn. Lôi hết ngày sinh của ông bà bố mẹ cụ kị nội ngoại ra chúng ta được một dãy số như sau:

```
data_2002 = get_data_range(0, 1)
loto_arr = [18, 5, 27, 6, 28, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 2]
print total_lost(test_data=data_2002, loto_arr=loto_arr, price=20000)

>>> -33600000
```

Quả này thua còn đau hơn lần trước nữa. Tổng số tiền chúng ta mất đi sau khi cày cuốc một năm đó là **33 triệu 600 ngàn VNĐ**. Tại sao vẫn như vậy. Giờ thì đánh thử một con thôi, dân trong nghề gọi là **bạch thủ** xem thử xem ra sao. 


## Thử ngẫu nhiên một con duy nhất
Giờ chúng ta thử chỉ chơi một con duy nhất xem sao. Ví dụ ngày sinh của bố mình chẳng hạn

```
loto_arr = [18]
print total_lost(test_data=data_2002, loto_arr=loto_arr, price=20000)

>>> -6720000
```

Thất bại có vẻ như ít nhất trong các lần chơi. Hình như có một điều được rút ra đó là:

> Nếu chọn ngẫu nhiên thì đánh càng nhiều thì sẽ thua càng nhiều

Đây là cách chơi mà những người chuyên nghiệp gọi là kiểu **gà mờ** tức là chẳng cần một tý kiến thức nào cả cũng có thể chơi được. Giờ chúng ta thử tìm cách khác xem sao


# Chơi xổ số kiểu thống kê

Chúng ta đã thấy rằng cách chơi **kiểu gà mờ** chỉ gây những thiệt hại to lớn cho chúng ta. Giờ chúng ta sẽ chơi theo một hướng đi khác, đó là sử dụng một số kĩ thuật thống kê vào chơi xổ số

## Dựa trên các số đề ra nhiều nhất

Một cách mơ hồ chúng ta có thể tin rằng các số ra nhiều nhất thì có khả năng sẽ đem lại cho chúng ta may mắn hơn. Giờ chúng ta thử viết một hàm lấy ra top 10 số đề của năm 2002

```
def get_top_loto(data, n_top = 3):
    counter = Counter(data).most_common(n_top)
    labels, values = zip(*counter)
    return np.array(labels)
    
data_2002 = get_data_range(0, 1)
loto_arr = get_top_loto(data_2002, n_top=10)
print loto_arr

>>> [14 73 78 79 97 98  6 10 37 39]
```

Chúng ta sẽ sử dụng dữ liệu này để **đánh đề** trong năm 2003 xem số tiền thu được có ổn hơn không nhé

```
data_2003 = get_data_range(1, 2)
print total_lost(test_data=data_2003, loto_arr=loto_arr, price=20000)

>>> -18600000
```

Căng thật số tiền nhận được vẫn không ăn thua lắm. Liệu rằng có phải do chúng ta đã có quá ít dữ liệu hay không. Hãy thử lấy top 10 số ra nhiều nhất từ năm **2002** đến năm **2015** và áp dụng để chơi trong năm **2016** xem có khả quan hơn không


```
data_2002_to_2015 = get_data_range(0, 14)
loto_arr = get_top_loto(data_2002_to_2015, n_top=10)
print loto_arr
data_2016 = get_data_range(14, 15)
print total_lost(test_data=data_2016, loto_arr=loto_arr, price=20000)

>>> [36 10  6 39 17  1 15 60 14 32]
>>> -25600000
```

Kết quả không khả quan hơn thậm chí còn tệ hơn nữa chứng tỏ vấn đề không phải là dữ liệu nhiều hay ít

## Để máy tính chọn hộ

Thôi thì chẳng tính toán gì nữa cả. Cách tốt nhất là nhờ máy tính chọn hộ, nó chọn số nào mình chơi số đó. Mặc đời trôi luôn. Chúng ta chỉnh lại một chút trong hàm ``total_lost`` như sau:


```
from random import randint

def total_lost(test_data, loto_arr = None, price = 0):
    total = 0
    for rs in test_data:
        rand = randint(0,99)
        lost = loto_lost_func(loto_arr=[rand], rs=rs, price=price)
        total += lost
    return total

data_2016 = get_data_range(14, 15)
print total_lost(test_data=data_2016, price=20000)

>>> -1160000
```

> **Nhận xét:** có vẻ như phương pháp lựa chọn ngẫu nhiên cho kết quả tốt nhất nhưng vẫn không thể sinh cho chúng ta một đồng lãi :cry:


# Bài học rút ra

Bây giờ bạn đã hiểu tại sao mà **Phan Thị Inc** nói không với ma túy nhưng lại tập trung hoạt động bảo kê mở sòng bạc chưa. Có lý do cả đó các bạn ạ. Sau bài này mình cảm thấy cần rút ra một số bài học đó là:

* Đừng có tìm quy luật cho những thứ ngẫu nhiên
* May mắn chỉ đến một vài lần trong đời (thường là rất hiếm) nên đừng hi vọng chúng ta có thể gặp nó hàng ngày
* Xổ số là lĩnh vực rất có lợi cho nhà đầu tư **(công ty xổ số)** chứ không bao giờ có lợi cho người chơi nó
* Vì sao nên chơi xổ số. Vì nó được tung hô là **ích nước lợi nhà** tức là tăng thêm thuế cho đất nước và tăng thu nhập cho **nhà đầu tư** tức **công ty xổ số** :heart_eyes: