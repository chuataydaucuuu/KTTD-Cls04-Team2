import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/login"
    

@pytest.fixture
def driver():
    # Mở trình duyệt Chrome trước mỗi bài test
    d = webdriver.Chrome()
    d.implicitly_wait(5)  # chờ tối đa 5 giây để phần tử xuất hiện
    d.get(URL)
    yield d
    d.quit()  # đóng trình duyệt sau mỗi bài test


def dang_nhap(driver, username, password):
    """Hàm dùng chung: nhập tên, nhập mật khẩu, bấm nút Login."""
    # 1. Tìm phần tử + 2. Thao tác với nó
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def test_dang_nhap_thanh_cong(driver):
    """TC01: đúng tên và mật khẩu -> vào được trang /secure."""
    dang_nhap(driver, "tomsmith", "SuperSecretPassword!")
    # 3. Kiểm tra kết quả
    thong_bao = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in thong_bao
    assert "/secure" in driver.current_url


def test_dang_nhap_sai_mat_khau(driver):
    """TC02: đúng tên, sai mật khẩu -> báo lỗi mật khẩu, ở lại /login."""
    dang_nhap(driver, "tomsmith", "saimatkhau")
    thong_bao = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in thong_bao
    assert "/login" in driver.current_url


def test_dang_nhap_sai_ten_dang_nhap(driver):
    """TC03: sai tên đăng nhập -> báo lỗi tên đăng nhập, ở lại /login."""
    dang_nhap(driver, "khongtontai", "SuperSecretPassword!")
    thong_bao = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in thong_bao
    assert "/login" in driver.current_url
