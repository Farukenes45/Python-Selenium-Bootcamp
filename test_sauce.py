# selenium modülünden webdriver import et
from selenium import webdriver

# chrome driver managerı import et
from webdriver_manager.chrome import ChromeDriverManager

# time modülünden sleep import et
from time import sleep

# By modulu verileri daha kolay alamaya yarar işimizi kolaylaştırır
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        # sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        # sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        # sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        # print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"test sonucu: {testResult}")
       
testClass = Test_Sauce()
testClass.test_invalid_login()
while True:
    continue