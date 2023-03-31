# liste tanımlama
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

# Listenin yazdırılması ve elemanlara erişim
print(krediler)
print(krediler[0])                         # Hızlı Kredi
print(krediler[1])                         # Maaşını Halkbank'tan alanlara özel
print(krediler[2])                         # Mutlu emekli ihtiyaç kredisi


print(len(krediler))                        # Listenin uzunluğu

# Listenin bir elemanının değiştirilmesi ve tekrar yazdırılması
krediler[0] = "Çabuk Kredi"                 # 0. indisteki değeri değiştirdik
print(krediler)
print(krediler[2])


for kredi in krediler:
    print("<option>" + kredi + "</option>")

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3, 10): 
    print(i)

for i in range(0, 11, 2): 
    print(i)



# 2. Canlı Dersten Bazı Notlar

# string interpolation
vade = int(input("istediğiniz vade yi belirtin: "))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {}".format(vade))
# bu şekilde format içine bir değişken adı tanımlayadabiliriz
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")
print("*"*50)
# listeler
krediler = ["ihtiyaç kredisi","Taşıt kredisi","Konut kredisi","Özel kredi"]
krediler.append("X kredisi")    # belirtilen değeri listenin sonuna ekler
print(krediler)
krediler.remove("Özel kredi")   # belirtilen değeri siler
print(krediler)
krediler.pop(0)                 # belirttiğimiz indeksteki değeri siler indeks belirtmezsek son elemanı siler
print(krediler)
krediler.extend(["Yeni Kredi1","Yeni Kredi2"])  # tek seferde birden çok değeri eklemeye yarar,1 argüman aldığı için dizi olarak tanımlarız.
#krediler.extend("Yeni Kredi1","Yeni Kredi2")   # bu kod hatalıdır fonksiyon 1 arguman alır hatası verir
print(krediler)

# döngüler
# 2 kodda aynı sonucu verir
kredi = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
for i in kredi:
    print(i)
print("************************")
for i in range(3):
        print(kredi[i])

# while döngüsü
# i değerini while döngüsü içinde farklı yerlerde arttırınca çıkan sonuç değişir
kredi = ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
print("***********************************")
i=0
while i<len(kredi):
    i+=1
    print(i)
    print(kredi[i])
    if kredi[i] == "konut kredisi":     #taşıt ve konut kredisini yazar
        break
print("***********************************")
i=0
while i<len(kredi):
    print(i)
    print(kredi[i])
    i+=1
    if kredi[i] == "konut kredisi":     # ihtiyaç ve taşıt kredisini yazar
        break

print("***********************************")
i=0
while i<len(kredi):
    if kredi[i] == "konut kredisi":     # ihtiyaç ve taşıt kredisini yazar
        break
    print(i)
    print(kredi[i])
    i+=1


# fonksiyonlar
print("FONKSİYONLAR BÖLÜMÜ")

def calculate():
    print("1.fonksiyon çıktısı: ",100-20)

def calculateParams(fiyat,indirim):
    print("2.fonksiyon çıktısı:",fiyat-indirim)


def sayHello(name):
    print("--> "f"Merhaba {name}")

def calculateAndReturn(price,discount):
    return price - discount


calculate()
calculateParams(50,20)
sayHello("Enes")
yeniFiyat = calculateAndReturn(100,50)
print(yeniFiyat)

print(" ***** RETURN TEKRAR *****")
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceReturn(price,discount):
    return price - discount

fonk1 = calculatePrice(100,50)              # 50 çıktısını verir
fonk2 = calculatePriceReturn(200,100)       # burda çıktı vermez değeri print etmeliyiz
print(f"103.Satır: {fonk1}")                # None değeri verir , fonksiyon geriye değer döndürmez
print(f"104.Satır: {fonk2}")                # 100 değerini verir fonksiyon geriye değer döndürmüştür

# print o anlık ekrana yazdırır değeri tutmaz bu yüzden üstünde değişiklik yapıp tekrar kullanamayız
# return de değeri değişkene atıp saklayabilirz,üzerinde değişiklik yapabiliriz, tekrar kullanabiliriz