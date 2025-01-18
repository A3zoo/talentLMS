Theo như yêu cầu bài toán và phương án đã chọn là phương án 3.

Mô tả ứng dụng Knowledge Bank là một ứng dụng để cho người dung truy cập vào để xem các thông tin huấn luyện sử dụng các dịch vụ (hình ảnh, video, text) và họ sẽ làm bài quiz để kiểm tra kiến thức của họ

Bên thứ 3 được chọn: Hệ thống talentLMS

Lý do tại sao chọn talentLMS:
- Course trong đây hỗ trợ đa dạng các kiểu nội dung (hình ảnh, video, text)
- Giao diện thân thiện người dùng.
- Hỗ trợ api để mở rộng ứng dụng.
- Hỗ trợ làm bài test (Thì bài test này chúng ta sẽ thực hiện bằng cách vào trực tiếp link của web, link này được đính kèm theo Course) (Hiện tại cũng chưa cần tích hợp chấm điểm vào hệ thống nên chúng ta sẽ ưu tiên thực hiện các chức năng khác)

-----> Từ những lý do đó ta có thể chọn phương án này

Em sẽ thiết kết back-end như sau:
- Các tính năng thêm, xóa, sửa đã có sẵn trên trang talentLMS và vậy ở đây em chỉ thiết kế chức năng <br>
++ get_courses: lấy toàn bộ khóa học<br>
++ get_a_course: Lấy khóa học theo id<br>
++ get_test: Lấy bài test của khóa học<br>
++ get_answer: Lấy kết quả đánh giá bài test<br>
- Xây dựng chức năng đăng nhập cho hệ thống (Simple OAuth2 with Password and Bearer).<br>
++ Sử dụng OAuth2PasswordBearer(tokenUrl="login")<br>
++ Trả về token cho người dùng<br>
++ Xác thực người dùng mỗi khi truy cập tới route<br>
(Tham khảo tại https://fastapi.tiangolo.com/tutorial/security/simple-oauth2)

Cấu trúc thư mục:
- Conttroller: là nơi chứa các route của ứng dụng.
- Models: sẽ là nơi định nghĩa cấu trúc của các đối tượng cần sử dụng trong ứng dụng.
- Services: đây là nơi chứa các logic nghiệp vụ của ứng dụng. Services thực hiện các công việc phức tạp và xử lý dữ liệu từ model.
- Utils: : Là nơi chứa các tiện ích hoặc hàm hỗ trợ mà có thể được sử dụng lại ở nhiều phần khác nhau trong ứng dụng. (Hỗ trợ giao tiếp với talentLMS thông qua api và xử lý lỗi )
- Tests: ây là nơi chứa các bài kiểm tra (tests) cho ứng dụng, giúp đảm bảo rằng các tính năng của ứng dụng hoạt động chính xác.


Các file:
- app: file chính thực thi của chương trình
- .env: Chứa các biến môi trường
và 1 số file khác

Cách chạy ứng dụng:
- Clone project: git clone https://github.com/A3zoo/talentLMS.git
- Tạo môi trường ảo python: https://python-forum.io/thread-39414.html
- install các thư viện cần thiết: pip install -r requirements.txt
- Run chương trình: uvicorn app:app --reload
- Thay vào biến môi trường TALENTLMS_API_KEY và TALENTLMS_BASE_URL
- Truy cập vào: http://127.0.0.1:8000/docs để vào giao diện Swagger UI



Các test case:
- Lấy thông tin từng khóa học
@router.get("/courses/{id}")
id = 125 or 124

- Lấy bài test
@router.get("/courses/{course_id}/test/{id}")
course_id = 125 & id = 2065 hoặc 2066

- Lấy kết quả test
@router.get("/courses/{course_id}/testanswer/{id}")
course_id = 125 & id = 2065 hoặc 2066


