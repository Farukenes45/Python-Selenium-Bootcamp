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
import openpyxl

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

    # Test Case1: Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    @pytest.mark.parametrize("username,password",[("","")])
    def test_empty_username_and_password(self,username,password):
        
        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_username_password_{username}_{password}.png")

        assert error_message.text == "Epic sadface: Username is required"

             
    # Test Case2: Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
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
        

    # Test Case3: Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
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

     
    # Test Case4: Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
    @pytest.mark.parametrize("username,password",[("close_icon_test","close-button")])
    def test_close_buton_icon(self,username,password):

        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")

        self.wait_for_element_visible((By.ID,"password"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test_close_buton_icon_{username}_{password}.png")

        icon_button = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        icon_button.click()

    # 3 adet geçersiz giriş deneme
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


    # Test Case5: Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
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

    # ürün ekleme ve sepeti gösterme
    @pytest.mark.parametrize("username,password",[("problem_user","secret_sauce")])
    def test_add_to_cart(self,username,password):

        self.wait_for_element_visible((By.ID,"user-name"))
        user_input = self.driver.find_element(By.ID,"user-name")
        
        self.wait_for_element_visible((By.ID,"password"))
        user_password = self.driver.find_element(By.ID,"password")

        user_input.send_keys(username)
        user_password.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        product_list = ["add-to-cart-sauce-labs-backpack","add-to-cart-sauce-labs-bike-light"]
 
        for product in product_list:

            self.wait_for_element_visible((By.ID,product))
            add_button = self.driver.find_element(By.ID,product)

            add_button.click()

            self.driver.save_screenshot(f"{self.folderPath}/test_add_to_cart_{username}_{password}.png")

        shopping_cart = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")

        shopping_cart.click()

        self.driver.save_screenshot(f"{self.folderPath}/test_shopping_cart_{username}_{password}.png")
       
        # elemanların görünür olması için gereken bekleme süresi
    def wait_for_element_visible(self,locator,timeout=3):
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

