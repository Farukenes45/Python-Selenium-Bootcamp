from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class SauceDemoTest:

    def __init__(self):
        print("demo çalıştı")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    # Test Case1: Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

    def test_empty_username_and_password(self):
        self.user_input = self.driver.find_element(By.ID,"user-name").send_keys("")
        self.user_password = self.driver.find_element(By.ID,"password").send_keys("")
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        self.loginBtn.click()
        self.error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.test_result = self.error_message.text == "Epic sadface: Username is required"
        print(f"Test Case1 result: {self.test_result}")
        sleep(3)
      
    # Test Case2: Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    def test_empty_password(self):
        self.user_input = self.driver.find_element(By.ID,"user-name").send_keys("Test Case2")
        self.user_password = self.driver.find_element(By.ID,"password").send_keys("")
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        self.loginBtn.click()
        self.error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.test_result = self.error_message.text ==  "Epic sadface: Password is required"
        print(f"Test Case2 result: {self.test_result}")
        sleep(3)

    # Test Case3: Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

    def test_locked_out_user(self):
        self.user_input = self.driver.find_element(By.ID,"user-name").send_keys("locked_out_user")
        self.user_password = self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        self.loginBtn.click()
        self.error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.test_result = self.error_message == "Epic sadface: Sorry, this user has been locked out"
        print(f"Test Case3 result: {self.test_result}")
        sleep(3)

    # Test Case4: Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.

    def close_buton_icon(self):
        self.user_input = self.driver.find_element(By.ID,"user-name").send_keys("")
        self.user_password = self.driver.find_element(By.ID,"password").send_keys("")
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        self.loginBtn.click()
        sleep(2)
        self.icon_button = self.driver.find_element(By.CSS_SELECTOR,"login_button_container > div > form > div:nth-child(1) > svg")
        self.icon_button.click()
        sleep(3)

    # Test Case5: Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def test_successfull_login(self):
        self.user_input = self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.user_password = self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(1)
        self.loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(5)
        # self.product = WebDriverWait(self.driver,5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"inventory_item")))
        self.product = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Toplam ürün sayısı: {len(self.product)}")


# SauceDemoTest().test_empty_username_and_password()            # test case1
# SauceDemoTest().test_empty_password()                         # test case2
# SauceDemoTest().test_locked_out_user()                        # test case3
# SauceDemoTest().close_buton_icon()                            # test case4
SauceDemoTest().test_successfull_login()                      # test case5 and 6

while True:
    continue
