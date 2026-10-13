from selenium import webdriver

def test_the_internet_title():
    # 1. Khởi tạo trình duyệt Google Chrome
    driver = webdriver.Chrome()

    # 2. Mở trang web kiểm thử theo yêu cầu đề bài
    driver.get("https://the-internet.herokuapp.com/")

    # 3. Lấy tiêu đề thực tế của trang hiện tại
    actual_title = driver.title

    # 4. Kiểm tra (assert) xem tiêu đề có đúng là 'The Internet' hay không
    assert actual_title == "The Internet", f"Lỗi: Tiêu đề nhận được là '{actual_title}'"

    # 5. Đóng trình duyệt sau khi kiểm tra xong
    driver.quit()