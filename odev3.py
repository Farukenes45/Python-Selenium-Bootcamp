# ÖDEV TANIMI:

# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


# ------------------------------ Öğrenci Ekleme ----------------------
ogrenci_listesi = []                

def addStudent():
    isim_soyisim = input("Eklemek istediğiniz öğrencinin isim ve soyismini girin: ")
    ogrenci_listesi.append(isim_soyisim)
    #return ogrenci_listesi
    print(ogrenci_listesi)

addStudent()
addStudent()

# ------------------------------ Öğrenci Silme ----------------------
def deleteStudent():
    isim_soyisim = input("Silmek istediğiniz öğrencinin adını girin: ")
    for ogrenci in ogrenci_listesi:
        if isim_soyisim == ogrenci:
            ogrenci_listesi.remove(isim_soyisim)
            print(f"Silinen Öğrencinin adı: {isim_soyisim}")

deleteStudent()

# ------------------------------ Çoklu Öğrenci Ekleme ----------------------
def multipleAddStudent():
    adet = int(input("Kaç adet öğrenci eklemek istersiniz ?:"))
    sayac = 0
    while sayac < adet:
        isim_soyisim =input("Eklemek istediğiniz öğrencinin adı ve soyadını girin:")
        ogrenci_listesi.append(isim_soyisim)
        #print(ogrenci_listesi)
        sayac+=1
        
multipleAddStudent()
print(f"--> Güncel Kayıtlı Öğrenci Listesi:{ogrenci_listesi}")

# name,surname = input("ad soyad girin")
# ogrenci = addStudent()
# print("17.satır: ", ogrenci)
# print(ogrenci_listesi)
# # print(ogrenci)
# print(len(ogrenci_listesi))



# listedeki tüm öğrencileri tek tek yazdıran fonksiyon
# def ogrencileriYazdir():
#     for kayitli_ogrenci in ogrenci_listesi:
#         print(kayitli_ogrenci)
#         return kayitli_ogrenci
    
# kayitli_ogrenciler = ogrencileriYazdir()



