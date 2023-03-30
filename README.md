
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
