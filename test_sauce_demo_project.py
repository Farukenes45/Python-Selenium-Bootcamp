from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Sauce_Demo:

     # her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        # günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur
        self.folderPath = str(date.today())
        #exist_ok_True ilgili path oluşturulmuş ise tekrar bunu oluşturma
        Path(self.folderPath).mkdir(exist_ok=True)

    # her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    # doğru kullanıcı adı - boş şifre kısmı girilirse
    @pytest.mark.parametrize("username,password",[("standard_user" , "")])
    def test_empty_password(self,username,password):

        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test_empty_password_{username}_{password}.png")

        assert error_message.text ==  "Epic sadface: Password is required"

    # yasaklanan kullanıcı adı - doğru şifre girişi
    @pytest.mark.parametrize("username,password",[("locked_out_user" , "secret_sauce")])
    def test_locked_out_user(self,username,password):

        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test_locked_out_user_{username}_{password}.png")

        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

     # 3 adet geçersiz kullanıcı adı ve şifre girilirse
    @pytest.mark.parametrize("username,password",[("deneme1" , "123") , ("deneme2" , "345") , ("deneme3" , "678")])
    def test_invalid_login(self,username,password):

        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"user-name"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        error_message = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")

        self.driver.save_screenshot(f"{self.folderPath}/test_invalid_login_{username}_{password}.png")
        
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

    # kullanıcı adı ve şifre doğru girilirse
    @pytest.mark.parametrize("username,password",[("standard_user" , "secret_sauce")])
    def test_successfull_login(self,username,password):

        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.get("https://www.saucedemo.com/inventory.html")

        self.wait_for_element_visible((By.CLASS_NAME,"inventory_item"))
        self.product = self.driver.find_elements(By.CLASS_NAME,"inventory_item")

        product_count = len(self.product)
        
        self.driver.save_screenshot(f"{self.folderPath}/test_successfull_login_{username}_{password}.png")
        
        assert product_count == 6

    def test_add_and_remove_product(self):

        self.test_successfull_login("standard_user", "secret_sauce")

        # 6 ürün ekle
        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"add-to-cart-sauce-labs-backpack\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"add-to-cart-sauce-labs-bike-light\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"add-to-cart-sauce-labs-onesie\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()

        
        shopping_basket = self.driver.find_element(By.LINK_TEXT,"6")
        shopping_basket.click()
        
        shopping_basket_url = self.driver.get("https://www.saucedemo.com/cart.html")
        self.wait_for_element_visible((By.ID,"page_wrapper"))
        
        self.driver.save_screenshot(f"{self.folderPath}/test_add_product.png")

        # 3 ürün sil
        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"remove-sauce-labs-backpack\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"remove-sauce-labs-bike-light\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").click()

        self.wait_for_element_visible((By.CSS_SELECTOR,"*[data-test=\"remove-sauce-labs-bolt-t-shirt\"]"))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bolt-t-shirt\"]").click()

        self.driver.save_screenshot(f"{self.folderPath}/test_remove_product.png")
        
        # checkout butonu
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
        checkout_button.click()

        self.driver.save_screenshot(f"{self.folderPath}/checkout_button_clicked.png")
        # information kısmı
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("faruk")

        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("enes")

        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("454545")
        
        self.driver.save_screenshot(f"{self.folderPath}/information.png")
        # continue butonu
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
        # finish butonu
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
        self.driver.save_screenshot(f"{self.folderPath}/finish.png")
        # back home butonu
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
        
    # elemanların görünür olması için gereken bekleme süresi
    def wait_for_element_visible(self,locator,timeout=3):
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
