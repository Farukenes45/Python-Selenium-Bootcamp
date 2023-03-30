
# PYTEST DECORATORS

Dekoratör, Python'da kullanıcının yapısını değiştirmeden var olan bir nesneye yeni işlevler eklemesine izin veren bir tasarım modelidir.
Dekoratörler genellikle dekore etmek istediğiniz bir fonksiyonun tanımından önce çağrılır.

Test fonksiyonlarında belirli durumları sağlamak ve engellemek için kullanılır. 

Pytest te kullanılan bazı dekoratörler 

@pytest.mark.parametrize = Farklı parametreler alarak testin birden fazla çalışmasını sağlar. Örneğin kullanıcı adı ve şifre durumlarında
birden fazla girdinin denenmesini verebiliriz.

@pytest.mark.skip = İlgili fonksiyon kısmının çalıştırılmadan geçilmesini sağlar.

@pytest.fixture = Test işlemlerinde tekrar edecek işlemleri tanımlamak için kullanılır.

@pytest.mark.skipif = Belirli koşullara dayalı testleri atlamak için kullanılabilen yerleşik bir skif işareti sağlar .
Koşul doğruysa atlanan testler yürütülmez ve test paketi başarısızlıklarına sayılmaz.

@pytest.mark.xfail = Bir xfail, bir testin herhangi bir nedenle başarısız olmasını beklediğiniz anlamına gelir.
Yaygın bir örnek, henüz uygulanmayan bir özellik veya henüz düzeltilmemiş bir hata için yapılan testtir.
Başarısız olması beklenmesine rağmen bir test başarılı olursa (pytest.mark.xfail ile işaretlenir), bu bir xpass'tır ve test özetinde raporlanır.

@pytest.mark.filterwarning = Belirli test öğelerine uyarı filtreleri ekleyerek hataların, uyarıların yakalanmasını sağlar.
Yakalanan hatalar ve uyarılar sayesinde daha sağlıklı ve başarılı testler gerçekleştirilir.

@pytest.mark.timeout = Bir testin belirli bir süre içinde çalışmasını sağlar ve belirtilen sürenin üzerine çıktığında testi durdurur.

@pytest.mark.usefixtures = Test fonksiyonlarına belirli bir fixture otomatik olarak eklemek için kullanılır.

# 5.Gün Ödev2 Ekran Görüntüleri

![test](https://user-images.githubusercontent.com/119695278/228984392-5989ec59-15e3-4929-a5e7-e32ee5c726f8.PNG)
![test_empty_username_password__](https://user-images.githubusercontent.com/119695278/228984416-dff5f41d-3078-4e63-a9a5-40ce97166fe6.png)
![test_empty_password_standard_user_](https://user-images.githubusercontent.com/119695278/228984412-aa6f9107-1a86-4c9d-93c6-9fcb63f5284c.png)
![test_locked_out_user_locked_out_user_secret_sauce](https://user-images.githubusercontent.com/119695278/228984364-1b5ec609-91b8-4824-838e-4b9ee9eb09da.png)
![test_close_buton_icon_close_icon_test_close-button](https://user-images.githubusercontent.com/119695278/228984406-c8722462-85d8-4904-80d5-6b58bb3c79b3.png)
![test_successfull_login_standard_user_secret_sauce](https://user-images.githubusercontent.com/119695278/228984384-a86a387c-26c4-4865-b688-68872a8d1f9c.png)
![test_shopping_cart_problem_user_secret_sauce](https://user-images.githubusercontent.com/119695278/228984375-0c8a8a47-9152-4277-97b4-8d10e60e9196.png)
![test_add_to_cart_problem_user_secret_sauce](https://user-images.githubusercontent.com/119695278/228984399-1354b5f8-beb6-47f2-9a47-203e5fcedb65.png)










