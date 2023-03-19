# selenium modülünden webdriver import et
from selenium import webdriver

# chrome driver managerı import et
from webdriver_manager.chrome import ChromeDriverManager

# time modülünden sleep import et
from time import sleep

# By modulu verileri daha kolay alamaya yarar işimizi kolaylaştırır
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

# tarayıcı tam ekran
driver.maximize_window()

# url tipi string
driver.get("https://www.google.com/")
sleep(5)
# input elemanının name değeri q olan değeri al
# input değişkenimizde artık farklı fonksiyonları kullanabiliriz
input = driver.find_element(By.NAME,"q")
# input.click() , input.send_keys() gibi
# print(f"Input: {input}")

# google input kısmına kodlamaio yazar
input.send_keys("kodlamaio")
# google da ara butonuna tıklama olayı
searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
# arattıktan sonra ilk kodlamaio sitesinde tıkladık xpath olarak o sitenin yolunu belirttik
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
courses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"kodlamaio sitesinde şu anda {len(courses)} adet kurs var")
# 10 sn uyu(bekle)
# sleep(10)

# google ekranımızın açılıp kapanmaması için sonsuz döngü oluşturduk
# kod buraya gelince sürekli çalışacağından sayfa kapanmaz
while True:
    continue
# HTML LOCATORS
# en tepeden başlayarak ilgilenen elemente kadar yolu belirtir
# full xpath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

# xpath
# //*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a

# find element ilk bulduğu locatörü ü döner
# fine elements liste halinde döner bulunan kaç adet eleman varsa
#geriye liste halinde döner

