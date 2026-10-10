# Ghi chú Tuần 4 - Team W...

## 1. Thành viên: Trần Trung Hiếu
- Điều đã học: Cách khởi tạo Selenium WebDriver, cách dùng pytest chạy test case và kiểm tra assertion.
- Trả lời câu hỏi:
  - Một script Selenium gồm các bước: Khởi tạo driver (dòng 5) --> Mở URL (dòng 8) --> Lấy thông tin trang (dòng 11) --> Kiểm tra điều kiện (dòng 14) --> Đóng trình duyệt (dòng 17).
  - pytest tự tìm test theo quy tắc: File có tiền tố test_*.py hoặc hậu tố *_test.py, bên trong tìm các hàm bắt đầu bằng test_*.
- Ghi chú lỗi:
        AssertionError: Lỗi: Tiêu đề nhận được là 'The Internet'
E       assert 'The Internet' == 'The Wrong Title'
E         
E         - The Wrong Title
E         + The Internet
