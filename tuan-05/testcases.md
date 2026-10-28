# Test case chức năng Đăng nhập (Tuần 5)

Trang kiểm thử: https://the-internet.herokuapp.com/login
Viết bằng lời, TRƯỚC khi viết code.

## TC01 - Đăng nhập thành công
- **Các bước làm:**
  1. Mở trang đăng nhập.
  2. Nhập tên đăng nhập vào ô Username.
  3. Nhập mật khẩu vào ô Password.
  4. Bấm nút Login.
- **Dữ liệu nhập:** username = `tomsmith`, password = `SuperSecretPassword!`
- **Kết quả mong đợi:** Chuyển sang trang `/secure`, hiện thông báo "You logged into a secure area!".

## TC02 - Đăng nhập thất bại: sai mật khẩu
- **Các bước làm:** Như TC01.
- **Dữ liệu nhập:** username = `tomsmith`, password = `saimatkhau`
- **Kết quả mong đợi:** Vẫn ở trang `/login`, hiện thông báo "Your password is invalid!".

## TC03 - Đăng nhập thất bại: sai tên đăng nhập
- **Các bước làm:** Như TC01.
- **Dữ liệu nhập:** username = `khongtontai`, password = `SuperSecretPassword!`
- **Kết quả mong đợi:** Vẫn ở trang `/login`, hiện thông báo "Your username is invalid!".

## Cách xác định phần tử (dùng DevTools của Chrome, F12)
| Phần tử | Cách tìm (locator) |
|---|---|
| Ô tên đăng nhập | `id = username` |
| Ô mật khẩu | `id = password` |
| Nút đăng nhập | `css = button[type='submit']` |
| Thông báo kết quả | `id = flash` |
