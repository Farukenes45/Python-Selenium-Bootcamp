
# pythonda veri tipleri nelerdir ?

# int(integer) -> tam sayı veri tipidir
tamsayi = 10
print(type(tamsayi))             # class int


# float -> ondalıklı(virgüllü) sayı veri tipidir
ondalikli_sayi = 3.14
print(type(ondalikli_sayi))      # class float


# string -> metinsel ifade veri tipidir. '' , " " , """ """ tırnakları arasında yazılır
metinsel_ifade = "Merhaba python öğreniyorum"
print(type(metinsel_ifade))      # class str


# Boolean -> True veya False olarak 2 değer alır
boolean = True
boolean2 = False
print(type(boolean))             # class bool
print(type(boolean2))            # class bool


# list -> Birden fazla veriyi ya da 1 den fazla farklı veri tipini bir arada tutmaya yarar
# integer değer tutan liste
my_list = [10,20,30,40,50]       # class list
print(type(my_list))


# string değer tutan liste
my_string = ["first name","last name","country"]
print(type(my_string))           # class list


# karmaşık değerleri tutan liste
complex_list = [11,"Hello",True,5.25,[5,15,25]]     # class list
print(type(complex_list))


# tuple(demet) -> listelerden farkı içinde bulunan değerler değiştirilemez
# listelerde olduğu gibi tuple içinde de birden fazla veya farklı değer tutmaya yarar
demet = (11,22,33,44,55)
print(type(demet))              # class tuple



# dictionary(sözlük) -> key ve value olarak tanımlanır,değiştirilebilir veri yapısıdır
my_dict = {"Name":"Faruk",
           "Surname":"Enes",
           "Age":"24",
           "city":"Manisa"}
print(type(my_dict))            # class dict
print(my_dict.keys())           # anahtarlara erişir                    ['Name', 'Surname', 'Age', 'city']
print(my_dict.values())         # anahtara karşılık gelen değere ulaşır ['Faruk', 'Enes', '24', 'Manisa']




# set(küme) -> matematikte kullandığımız küme kavramının pythondaki karşılığıdır
# kesişim , alt küme , üst küme , birleşim vs. özelliklerini bulabiliriz.

# kümeleri set() keyword ü ile ya da {} ile tanımlayabiliriz.
# {} ancak boş olarak tanımlarsak sözlük olarak algılanır. İçine değer atayarak küme tanımlayabiliriz.

kume = set()                                    # boş bir küme tanımlar
kume1 = {1,2,3,4,5}                             # dolu bir küme tanımlar
print(type(kume))                               # class set
print(type(kume1))                              # class set

# kümeye eleman ekleme
kume1.add(6)
kume1.add(7)
print(kume1)                                    # {1, 2, 3, 4, 5, 6, 7}

# kümeden eleman silme
kume1.remove(7)
kume1.remove(5)
print(kume1)                                    # {1, 2, 3, 4, 6}


# difference() : İlk kümede olup ikinci kümede olmayan elemanları bulmak için kullanılır.
A = {1,3,5,7,9}
B = {2,3,4,6,8,9}
print(f"A kümesinin B kümesinden farkı:{A.difference(B)}")  # {1, 5, 7}
# alternatif
print(f"A kümesinin B kümesinden farkı:{A-B}")              # {1, 5, 7}

# intersection(): 2 kümede ortak elemanları bulmak için kullanılır -KESİŞİM

# isdisjoint(): 2 kümenin ortak elemanı var mı yok mu sorgulanır,eğer ki hiç ortak eleman yoksa True
# aksi halde False sonucu verir -AYRIK KÜME

# issubset():bir kümedeki elemanların hepsinin başka bir küme içerisinde var olup olmadığını sorgular, -ALT KÜME

# issuperset(): Bir küme diğer bir kümedeki tüm elemanları içeriyor mu bunu sorgular,eğer ki içeriyorsa
# True aksi halde False sonuç verir -ÜST KÜME

# union(): 2 kümenin birleşimini bulmak için kullanılır. -BİRLEŞİM

# difference(): 2 kümenin farkını verir


k1 = {1,2,3,4}
k2 = {1,2,3,4,5,6}

print(k1.intersection(k2))      # 1 2 3 4      kesişim
print(k2.intersection(k1))      # 1 2 3 4

print(k1.isdisjoint(k2))        # False        ayrık küme
print(k2.isdisjoint(k1))        # False

print(k1.issubset(k2))          # True         alt küme
print(k2.issubset(k1))          # False

print(k1.issuperset(k2))        # False        üst küme
print(k2.issuperset(k1))        # True

print(k1.union(k2))             # 1 2 3 4 5 6  birleşimini verir
print(k2.union(k1))             # 1 2 3 4 5 6



"""
Görmüş olduğumuz tüm metinsel ifadeler(string) dersin adı ,butonlardaki metinler(öceki ders , bitir devam et)
değerlendirme , ders programı , ödev 1 ve 2 yazıları vs.

Ders programının ilerleyişine göre progress barın artması integer değer ( %75 Tamamlandı , %100 Tamamlandı)

Kategori ve Eğitmen kısımlarında bulunan dropbox içindeki değerler liste veri tipinde tutuluyor olabilir.

Kodlama.io sitesine kayıt olmadan kursun video ve ödevlerine erişemeyiz (şart blokları)

Login kısmındaki mail password bilgisi şart bloğudur
Kullanıcının doğru bilgileri girmesi sonucu siteye giriş yapılır

Siteye ilk kayıt olurken şifreyi 2 kere girip confirm etmek 2 şifre biribirine eşitmi (şart blokları)

Password yanında bulunan göz işareti şifreyi göster , gizle özelliği şart koşulu olabilir

"""

# Siteye girerken basit bir şart bloğu kodu
print("*"*50)

basarili_giris = True                                                   # True boolean değeri tanımladım

while basarili_giris:                                                   # while True olduğu için sonsuz döngüye girdi
    mail_adress = input("Mail adresinizi yazın: ")                      # mail bilgisi aldık
    password = input("Şifrenizi Girin: ")                               # şifre bilgisi aldık

    if mail_adress == "anonim@gmail.com" and password == "12345":    # girdiğimiz bilgiler doğrumu kontrol ettik
        basarili_giris = False                                          # mail ve şifre bilgimizi doğru girdiysek değeri False yaptık ve döngüden çıktık
        print("Giriş Yapılıyor...")
    else:                                                               # Mail veya şifreden birini yanlış girersek while döngüsü biz doğru değer girene kadar devam eder                                        
        print("Tekrar deneyin hatalı bilgi girdiniz !!")



