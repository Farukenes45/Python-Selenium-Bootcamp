"""
ÖDEV TANIMI:

HTML
HTML Locators
Selenium'da aksiyonlar (send_keys, click vb..)

------------------------------------------------------------------------------------------------------------
--> HTML NEDİR?

HTML BİR İŞARETLEME DİLİDİR , WEB SAYFALARINDA BULUNAN METİNLER,BUTONLAR,LİNKLER,FORM VS. YAPILAR HTML İLE OLUŞTURULUR.
WEB SAYFALARIMIZIN İSKELET YAPISINI OLUŞTURURKEN KULLANIRIZ. DAHA SONRA CSS VE KÜTÜPHANELERİYLE BİRLİKTE GÖRÜNÜMÜ DAHA GÜZEL HALE GETİREBİLİRİZ.
YAZILIM DİLLERİYLEDE STATİK YAPIDA OLAN YAPIMIZI DİNAMİK HALE GETİRİRİZ.

------------------------------------------------------------------------------------------------------------
--> Locators, web otomasyonu için kullanılan bir araçtır ve web sayfalarındaki HTML öğelerinin belirlenmesine yardımcı olur.
Otomasyon araçları, web sayfalarını otomatik olarak test etmek, veri toplamak veya otomatik olarak işlem yapmak için kullanılır
ve bu işlemler için HTML öğelerini bulmak ve etkileşim kurmak gerekir.

--> Locators, belirli bir HTML öğesini bulmak için kullanılan yol tarifidir. Selenium WebDriver gibi bir otomasyon aracı kullanırken,
belirli bir HTML öğesine erişmek için kullanabileceğiniz farklı locator türleri vardır. Bazı yaygın locator türleri şunlardır:

--> ID: HTML öğesinin benzersiz kimliğiyle eşleşir
--> Name: HTML öğesinin adıyla eşleşir
--> Class Name: HTML öğesinin sınıf adıyla eşleşir
--> Tag Name: HTML öğesi türüyle eşleşir
--> Link Text: Bağlantı metniyle eşleşir
--> Partial Link Text: Bağlantı metninin bir kısmıyla eşleşir
--> CSS Selector: CSS özellikleriyle eşleşir
--> XPath: XML yolu belirleyicisiyle eşleşir

Bu locator türleri, otomasyon araçlarının HTML öğelerini bulmak ve etkileşim kurmak için kullanabileceği farklı yöntemlerdir.

--> Peki istediğimiz ögelere nasıl ulaşabiliriz ?
İstediğimiz nesneye sağ tıkla ile incele(inspect) alanına tıklıyoruz. 
İncele(inspect) alanına tıkladıktan sonra objenin attribute’lerini görecebiliriz.

Ya da otomasyon yazacağımız site içerisinde klavyeden F12’ye basarak geliştirici seçeneklerine ulaşıyoruz.
Burada Elements sekmesine girerek web sayfası içinde bulunan elementlere ulaşabiliriz.
Elements sekmesinde bulunan ögelerin üstüne gelip sağ tık yaparak Copy sekmesinden ilgili elementin locatorünü istediğimiz yapıda alabiliriz.
Örnek: Copy element , Copy XPath , Copy Selector , Copy JS Path vs.

------------------------------------------------------------------------------------------------------------

--> Seleniumda kullanılan aksiyonlar

--> webdriver sınıfı, kullanılacak tarayıcıyı başlatmak için kullanılır.
from selenium import webdriver
driver = webdriver.Chrome()

--> get() metodu, belirtilen URL'ye gitmek için kullanılır.
driver.get("https://www.example.com")

--> find_element() metodu : html ögelerini bulmak için kullanılır.
Daha sonra, bulunan elementlere tıklama, metin gönderme, metin alma, elementin özelliklerini alma gibi etkileşimler gerçekleştirebilirsiniz.
usernameInput = driver.find_element(By.ID,"user-name")

--> find_elements() metodu, kaç adet eleman var ise bize bir dizi olarak döndürür.
courses = driver.find_elements(By.CLASS_NAME,"course-listing")

--> current_url, title gibi yöntemler, mevcut sayfa URL'sini ve başlığını alma gibi işlemler için kullanılır.
current_url = driver.current_url
title = driver.title

--> Sayfalar arasında gezinmek için back(), forward() ve refresh() metotları kullanılır.
driver.back()
driver.forward()
driver.refresh()

--> save_screenshot() metodu, web sayfasının ekran görüntüsünü alır ve belirtilen bir dosya yoluna kaydeder.
driver.save_screenshot("example.png")

--> send_keys() metodu,öğenin type özelliği kullanılarak metin kutularına, parola alanlarına, arama kutularına vb. metin göndermek için kullanılabilir.
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Python Selenium")

"""

