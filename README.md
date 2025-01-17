Theo như yêu cầu bài toán và phương án đã chọn là phương án 3.

Bên thứ 3: Hệ thống talentLMS
Mô tả ứng dụng Knowledge Bank là một ứng dụng để cho người dung truy cập vào để xem các thông tin huấn luyện sử dụng các dịch vụ (hình ảnh, video, text) và họ sẽ làm bài quiz để kiểm tra kiến thức của họ

Lý do tại sao chọn talentLMS:
- Course trong đây hỗ trợ đa dạng các kiểu nội dung (hình ảnh, video, text)
- Giao diện thân thiện người dùng.
- Hỗ trợ api để mở rộng ứng dụng.
- Hỗ trợ làm bài test (Thì bài test này chúng ta sẽ thực hiện bằng cách vào trực tiếp link của web, link này được đính kèm theo Course) (Hiện tại cũng chưa cần tích hợp chấm điểm vào hệ thống nên chúng ta sẽ ưu tiên thực hiện các chức năng khác)

-----> Từ những lý do đó ta có thể chọn phương án này

Em sẽ thiết kết back-end như sau:
- Các tính năng thêm, xóa, sửa đã có sẵn trên trang talentLMS và vậy ở đây em chỉ thiết kế chức năng get_courses, get_one_course,... các tính năng để hiển thị thông tin lên cho khách hàng.
- Xây dựng chức năng đăng nhập cho hệ thống sử dụng jwt.

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

