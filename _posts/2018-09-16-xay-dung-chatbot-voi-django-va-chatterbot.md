---
title: "Blog #13 - Xây dựng chatbot tự động chat trên Chatwork với Chatterbot và Django"
last_modified_at: 2017-10-06T16:20:02-05:00
categories:
  - Recommendation
tags:
  - Recommendation System
teaser: 'https://cdn-images-1.medium.com/max/1200/1*RWHxIXnOrhsOAxmlDmCpDg.png'

excerpt: 'Xin chào tất cả các bạn, dạo gần đây mình thấy khá là nhiều bài viết liên quan đến chủ đề Chatbot trên Viblo tuy nhiên đa phần nội dung đều không nói rõ cách thực hiện Chatbot và deploy chatbot như thế nào. Đại đa số sử dụng một vài framework khá ăn liền như API của Simsimi hay Facebook Messenger điều này có một hạn chế là các bạn sẽ không tự custom nội dung được và một số API Chatbot như Simsimi còn bị giới hạn request nếu dùng free nữa. Bài viết hôm nay mình sẽ viết một bài viết để hướng dẫn các bạn xây dựng một ứng dụng Chatbot để trò chuyện trực tiếp trên Chatwork giúp các bạn giải trí hoặc giải quyết một số nhu cầu công việc của các bạn. Cũng giống như các bài hướng dẫn trước đây mình sẽ hướng dẫn các bạn từ bước sơ khai đến tận bước deploy hệ thống thực nên có thể sẽ khá dài nên mọi người chịu khó đọc hết nha. OK không dài dòng nữa chúng ta bắt đầu thôi.'

sidebar:
  nav: "docs"

---
{% include toc %}
Xin chào tất cả các bạn, dạo gần đây mình thấy khá là nhiều bài viết liên quan đến chủ đề Chatbot trên Viblo tuy nhiên đa phần nội dung đều không nói rõ cách thực hiện Chatbot và deploy chatbot như thế nào. Đại đa số sử dụng một vài framework khá ăn liền như **API của Simsimi** hay **Facebook Messenger** điều này có một hạn chế là các bạn sẽ không tự custom nội dung được và một số API Chatbot như Simsimi còn bị giới hạn request nếu dùng free nữa. Bài viết hôm nay mình sẽ viết một bài viết để hướng dẫn các bạn xây dựng một ứng dụng **Chatbot** để trò chuyện trực tiếp trên **Chatwork** giúp các bạn giải trí hoặc giải quyết một số nhu cầu công việc của các bạn. Cũng giống như các bài hướng dẫn trước đây mình sẽ hướng dẫn các bạn từ bước **sơ khai** đến tận bước deploy hệ thống thực nên có thể sẽ khá dài nên mọi người chịu khó đọc hết nha. OK không dài dòng nữa chúng ta bắt đầu thôi. 

# Chatbot là gì?

![](https://cdn-images-1.medium.com/max/1200/1*RWHxIXnOrhsOAxmlDmCpDg.png)

Chắc hẳn chatbot không còn làm cụm từ quá xa lạ với mọi người, hiểu nôm na đó chính là một **phần mềm** có thể thực hiện trò chuyện một cách tự động. Nó là một trong những ứng dụng khá đơn giản của **Machine Leanring** nhưng cũng đem lại những trải nghiệm hết sức thú vị. Chatbot xuất hiện rất nhiều trên các trang mạng xã hội, các trang bán hàng hay trong các dịch vụ chăm sóc khách hàng của các công ty. Bài viết này hôm nay mình không đề cập đến những kiến thức sâu trong **Chatbot** hay về xử lý ngôn ngữ tự nhiên mà mục đích của bài viết này giúp cho các bạn nào chưa hề biết gì về chatbot cũng có thể xây dựng được một chatbot của riêng mình. Nền tảng mình mình áp dụng cho việc xây dựng Chatbot lần này được mang tên là **ChatterBot** các bạn có thể tham khảo nó ở [đây](https://chatterbot.readthedocs.io/en/stable/tutorial.html). Bây giờ chúng ta sẽ bắt đầu ngay thôi. 

# Tiến hành cài đặt môi trường.

Trước tiên các bạn cần phải cài đặt môi trường để làm việc với ứng dụng của chúng ta. Ở đây mình sử dụng ngôn ngữ Python nên mình sẽ sử dụng một **virtualenv** của python để tạo một môi trường ảo cho riêng mình. Các bạn có thể tạo nó như sau:

```
 virtualenv -p python3 ~/chatbot
```

sau đó active môi trường để bắt đầu 

```
source ~/chatbot/bin/activate
```

Tiếp sau đó các bạn cần cài đặt các dependecies cần thiết. Ở đây mình ví dụ với package **chatterbot** của chúng ta.

```
pip install chatterbot
```
Ngoài ra để thực hiện các ví dụ trong bài blog này mình khuyến khích các bạn nên sử dụng [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html)
OK vậy là giờ các bạn đã có thể tiến hành training con bot của chúng ta được rồi. 

# Tiến hành training chatbot.

## Bước 1: Định nghĩa chủ đề của Chatbot

Đầu tiên để có thể dạy được một Chatbot tốt các bạn cần định nghĩa chủ đề của nó, ví dụ như các bạn muốn dạy một chatbot để có thể trả lời các câu hỏi trong công việc thường ngày thì các bạn cần phải dạy chatbot được những câu hỏi. Mục đích của nó là học xem với từng câu hỏi này thì mục đích của chúng ta đang hỏi là gì và từ đó tìm ra câu trả lời cho phù hợp. Ví dụ như

> Hôm nay có những ai đi làm -> đang hỏi về lịch làm việc 
> Hôm qua có những ai chưa báo cáo -> đang hỏi về tên những người chưa báo cáo
> 
Tùy thuộc vào mục đích việc xây dựng chatbot các bạn có thể thu thập dữ liệu theo các cách khác nhau tùy thuộc vào từng chủ đề khác nhau. Dưới đây là một mẫu ví dụ cho một chatbot được sử dụng để hỏi các thông tin trên chatwork:

```
conversation = [
    "Xin chào",
    "greeting",
    
    "Xin chào em",
    "greeting",
    
    "Chào em",
    "greeting",
    
    "Hello em",
    "greeting",
    
    "Hi em",
    "greeting",
    
    "Hôm qua có những ai quên chưa report em nhỉ",
    "forget_report_yesterday",
    
    "Hôm qua có những ai quên chưa báo cáo em nhỉ",
    "forget_report_yesterday",
    
    "Ai quên chưa report hôm qua",
    "forget_report_yesterday",
    
    "Ai chưa báo cáo hôm qua",
    "forget_report_yesterday",
    
    "Ai quên chưa báo cáo hôm qua",
    "forget_report_yesterday",
    
    "Ai quên  báo cáo hôm qua vậy em",
    "forget_report_yesterday",
    
    "Hôm nay ai đi làm thế",
    "today_work_schedule",
    
    "Hôm nay những ai đi làm thế",
    "today_work_schedule",
    
    "Hôm nay người nào đi làm thế",
    "today_work_schedule",
    
    "Hôm nay bạn nào đi làm thế",
    "today_work_schedule",
    
    "Lịch làm việc hôm nay",
    "today_work_schedule",
    
    "Lịch làm việc hôm nay thế nào",
    "today_work_schedule",
    
    "Những ai đi làm việc ngày hôm nay thế",
    "today_work_schedule",
]
```

Chúng ta có thể thấy mỗi câu hỏi được sắp xếp vào từng chủ đề khác nhau như chào hỏi hoặc kế hoạch làm việc ngày hôm nay. Điều nay tương đương như việc các bạn training một bộ phân lớp văn bản. Sau khi có được kết quả của bộ phân lớp này chúng ta sẽ có thể tìm được cách trả lời cho câu hỏi của người dùng. Mình không đi quá sâu vào phần này bởi sẽ làm ảnh hưởng đến tính thực tế của ứng dụng. Các bạn có thể tự xây dựng cho mình một tập các câu chủ đề riêng nhé.  

## Bước 2: Huấn luyện chatbot

Sau khi các bạn có tập dữ liệu thì việc tiếp theo cũng rất quan trọng đó chính là huấn luyện chatbot để có thể hiểu được nội dung của câu hỏi. Chúng ta đã thống nhất từ đầu là sẽ sử dụng thưu viện **chatterbot** giúp cho việc training này trở lên đơn giản hơn như sau:

```
from chatterbot import ChatBot

chatbot = ChatBot(
    "Chatwork Bot",
    database='db.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': "(no)"
        },
    ],
)
```

Các bạn có thể thấy rằng chúng ta sẽ khai báo một chatbot. Kết quả training của chatbot này được lưu tại **db.sqlite3**. Chúng ta add thêm một vài xử lý logic cho việc nhận dạng chatbot đó chính là 

* **BestMatch**: lựa chọn một câu trả lời có độ tương tự nhất với câu lệnh đã cho. Có thể hình dung đơn giản như sau, sau khi nhận vào một câu hỏi, chatbot sẽ tìm kiếm trong tập các câu hỏi và tính toán độ tương tự dựa trên một khoảng cách gọi là **edit distance** rồi sử dụng một hàm khác, có thể định nghĩa theo logic của chúng ta để đưa ra câu trả lời phù hợp
* **LowConfidenceAdapter** tham số này trả về một câu trả lời mặc định được chỉ định nếu không thể xác định phản hồi với số lượng tin cậy cao. Giống như trên cài đặt của mình đó chính là từ **(no)** với ngưỡng **thresshold là 0.5**

Sau khi cài đặt và đã thu thập đủ dữ liệu cho chatbot chúng ta tiến hành training cho chatbot này.

```
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
```

Các bạn sẽ đợi cho đến khi chatbot training xong. Tùy thuộc vào tập dữ liệu của các bạn lớn hay nhỏ mà thời gian training cũng tăng lên tương ứng. 
## Bước 3: Lưu chatbot

![](http://www.clker.com/cliparts/S/2/X/6/z/D/save-to-database-hi.png)
Sau khi training xong chatbot sẽ tự động lưu vào file **db.sqlite3**. Các bạn có thê lưu trữ lại file này để sử dụng trong các trường hợp khác nhau. Bước này tương đương với việc lưu ra các model sau khi training mô hình bằng tensorflow hay pytorch. Bước tiếp theo chúng ta sẽ cùng test hoạt động cảu chatbot này nhé.
## Bước 4: Test saved chatbot

Sau bước lưu được chatbot, chúng ta sẽ tiến hành test thử hoạt động của chatbot này như thế nào nhé:


```
chatbot = ChatBot(
    "Chatwork Bot",
    database=CHATBOT_DATABASE,
    read_only = True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.6,
            'default_response': "default_response"
        },
    ],
)
```

trong đó **CHATBOT_DATABASE** là đường dẫn đến file chatbot mà chúng ta vừa mới lưu lại trên bước trước. Mọi người để ý tham số `read_only = True,` quy định chúng ta đang sử dụng chatbot này dưới dạng **đã được training**. Sau đó chúng ta có thể thử test nó bằng câu lệnh đơn giản như sau:

```
chatbot.get_response("Chào em")

>>> Chào anh em có thể giúp gì anh ạ.
```

OK vậy giờ chatbot của chúng ta đã có thể hoạt động được tuy nhiên muốn tích hợp nó với các ứng dụng bên ngoài thì đồi hỏi chúng ta phải viết code xử lý phần backend thông qua một framework nào đó để tạo API. Ở đây mình lựa chọn Django để viết backend và tận dụng luôn nền tảng Chatwork để viết frontend demo cho các bạn. 

# Làm việc với Chatwork API
## Tạo tài khoản cho chatbot
Trước hết bước đầu tiên các bạn cần làm đó là tạo cho chatbot một tài khoản Chatwork. Bạn hãy hình dung như khi chúng ta kết bạn với tài khoản này và trò chuyện như một người bình thường, chỉ có điều khác rằng những câu trả lời ở đây là do chatbot của chúng ta tạo ra thôi. Các bạn tiến hành đăng kí tài khoản như bình thường thôi. Bước này khá đơn giản

![](https://images.viblo.asia/3cc6e507-0728-4707-af32-7717cf1bb011.png)

Cứ next next next là được nhé.
## Tạo API Key cho chatbot

Sau khi các bạn đã tạo xong tài khoản cho chatbot. Việc tiếp theo là request API key cho nó. Request API này để làm gì, mục đích của nó là để bạn có thể trả lời các tin nhắn thông qua chatbot phía backend cũng như lấy các thông tin khác nữa. Việc này các bạn có thể thực hiện trong phần **API Settings -> API Token** sau đó các bạn tiến hành nhập mật khẩu để hiển thị API Key. Nếu như lần đầu bạn làm chuyện này thì bạn sẽ phải chờ Chatwork approve và tạo API Key cho bạn. Các lần sau thì đơn giản thôi. Lưu ý là hãy giữ bí mật API Key này nhé, không thì cả thế giới đều có thể sử dụng Chatwork của bạn đó:

![](https://images.viblo.asia/af210a99-ab45-4e10-8c57-5eb5b24c2f51.png)

Sau khi các bạn đã tạo API Key thành công thì chúng ta đi đến bước tiếp theo là tạo Web Hook Chatwork.
## Cài đặt Chatwork Webhook
Hiểu đơn giản thì Chatwork Webhook giúp chúng ta có thể handler các sự kiện diễn ra đối với tài khoản của mình một cách đơn giản hơn. Ví dụ như khi có người TO đến tài khoản chatbot trên Chatwork thì sẽ thực hiện việc gửi API lấy thông tin từ backend và trả lời lại tin nhắn. Để thực hiện được điều này Chatwork cung cấp cho chúng ta một công cụ là **Chatwork Webhook**. Các bạn có thể tạo mới Webhook tại **API Settings -> Webhook**. Nhờ việc sử dụng ChatWork Webhook chúng ta không cần thiết gọi Chatwork API định kỳ (Polling) để kiểm soát event mà vẫn có thể nhận thông báo ở real time. Và vì có thể tạo function liên kết với service bên ngoài như tương tác Bot thao tác trên Chatwork một cách đơn giản nên mình đã sử dụng nó trong bài hướng dẫn này. Tạo mới một Webhook các bạn sẽ trông thấy giao diện như sau:

![](https://images.viblo.asia/c4995e8c-a57f-4af5-9fa1-4a74ecbe39f9.JPG)

Có một vài thông tin cơ bản các bạn cần lưu ý:

* Để Account Type là Mention To You để mọi tin nhắn gửi để tài khoản Chatbot này đểu được handler. 
* Giữ bí mật Token của các bạn
* Webhook URL để gọi API xử lý tại phần backend. Mình sẽ nói rõ hơn phần này trong phần tiếp theo. Thông thường nó chính là URI sau khi bạn đã deploy lên server của bạn. Tuy nhiên nếu bạn đang test ở Local bạn có thể sử dụng công cụ là [ngrok](https://ngrok.com/) để kiểm tra. Giờ chúng ta sẽ bắt đầu sang phần quan trọng nhất đó chính là viết code Backend cho Chatbot này.

## Tìm hiểu cấu trúc request của Webhook 

Thông báo event từ ChatWork Webhook sẽ được tiến hành dựa vào request HTTPS POST tới Webhook URL đã được setting ở Màn hình quản lý Webhook. Chúng ta cùng xem xét đến cấu trúc Header của request trên Webhook:

![](https://images.viblo.asia/1d2811a7-563c-4045-8ec8-af00f39c81a2.png)

Trong đó body được gửi lên dưới dạng một chuỗi JSON có các mục như sau:

![](https://images.viblo.asia/31f71965-331e-4d74-9b8e-d193f4168dbe.png)

Ví dụ như:

```
{
    "webhook_setting_id": "12345",
    "webhook_event_type": "mention_to_me",
    "webhook_event_time": 1498028130,
    "webhook_event":{
        "from_account_id": 123456,
        "to_account_id": 1484814,
        "room_id": 567890123,
        "message_id": "789012345",
        "body": "[To:1484814]Okazu là gì?",
        "send_time": 1498028125,
        "update_time": 0
    }
}

```
Có một lưu ý là việc phải xác minh chữ kí mỗi lần gửi request. Cách xác minh của nó như sau:

> Lấy byte string đã decode BASE64 token làm secret key để lấy giá trị digest của request body dựa vào thuật toán HMAC-SHA256.
> Xác nhận string đã encode BASE64 giá trị digest đồng nhất với signature (Gía trị của X-ChatWorkWebhookSignature header) được cấp cho request header.
> Có thể xác minh bằng Token ở màn hình edit Webhook.

Các bạn cứ yên tâm, nếu thấy loằng ngoằng quá có thể sử dụng luôn code của mình phía dưới cũng được nhé. 
# Viết Backend API 

Toàn bộ backend API được triển khai trên framework là **Django**. Đây là một framework mạnh mẽ hỗ trợ cho người dùng viết web và giao diện và API khá mạnh mẽ. Mình sẽ không đi quá sâu vào framework này mà chỉ hướng đẫn cho các bạn vài hàm cơ bản để sử dụng thôi nhé:

## Validate request từ Webhook

Giống như đã nêu ở bên trên thì mỗi lần gửi request các bạn đều phải validate xem request đó có là request hợp lệ hay không (có bị giả mạo không). Bước này thực hiện như sau:

```
def validate_request(request):
    # Check the X-Hub-Signature header to make sure this is a valid request.
    chatwork_signature = request.META['HTTP_X_CHATWORKWEBHOOKSIGNATURE']
    chatwork_signature = bytes(chatwork_signature, encoding='utf-8')
    signature = hmac.new(settings.CHATWORK_WEBHOOK_SECRET, request.body, hashlib.sha256)
    expected_signature = base64.b64encode(signature.digest())

    if not hmac.compare_digest(chatwork_signature, expected_signature):
        return 0
    return 1
```

## Hàm xử lý request 

```
def handle_payload(payload):
    # More excute here

def decode_payload(request):
    payload = str(request.body, encoding='utf-8')
    return json.loads(payload)

@csrf_exempt
def handle_chatwork_webhook(request):
    if validate_request(request) == 0:
        return HttpResponseForbidden('Invalid signature header')
    payload = decode_payload(request)
    handle_payload(payload)
    return HttpResponse('Webhook received', status=200)
```
Chúng ta sẽ thấy hàm trên sẽ thực hiện validate request. Nếu request là hợp lệ thì tiến hành xử lý payload trong hàm handle_payload. Đến bước này các bạn hoàn toàn có thể sử dụng hàm test chatbot bên trên để tìm ra câu trả lời phù hợp. Mình không đi quá sâu vào phần này nhé. Việc xử lý các bạn có thể tham khảo trực tiếp trên mã nguồn của mình cung cấp phía dưới


# Deploy Heroku
Đến bước này các bạn có thể deploy ứng dụng của mình lên trên Heroku nhé. Nếu các bạn chưa rõ có thể tham khảo tại [đây](https://devcenter.heroku.com/articles/deploying-python)
# Source code

Toàn bộ source code các bạn có thể tham khảo tại [đây](https://github.com/thandongtb/chatwork_webhook)

# Test kết quả 

Mọi người có thể xem qua đoạn trò chuyện của mình và cô bạn **Chatbot** này nhé. Mình đã training bạn ấy để hỏi về lịch làm việc của team mình thông qua API của Doodle và các bạn cũng có thể làm việc với nhiều chức năng hơn thế. Rất là thú vị phải không nào 

{@embed: https://www.youtube.com/watch?v=C_ZjevM_Quw&feature=youtu.be}
            