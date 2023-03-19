class Matematik:
    # self ten kasıt matematiğin kendisi self
    # constructor - yapıcı blok
    def __init__(self,sayi1,sayi2):                     # Matematik() parantezinin çalışmasını init sağlar
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı (referans oluştu)")        
       
    def topla(self):
        return self.s1 + self.s2
    
    def cikar(self):
        return self.s1 - self.s2
    
    def bolme(self):
        return self.s1 / self.s2
    
    def carpma(self):
        return self.s1 * self.s2
    
matematik = Matematik(6,7)
toplama = matematik.topla()
cikarma = matematik.cikar()
bolme = matematik.bolme()
carpma = matematik.carpma()
print(toplama)
print(cikarma)
print(bolme)
print(carpma)

class Person:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age

musteri_1 = Person("Faruk","Enes",24)
musteri_2 = Person("Ahmet","Demiroğ",30)
musteri_3 = Person("Engin","Demiroğ",32)

# Musterinin adı: Faruk, Musterinin soyadı: Enes , Musterinin yaşı: 24
print(f"Musterinin adı: {musteri_1.name}, Musterinin soyadı: {musteri_1.lastname} , Musterinin yaşı: {musteri_1.age} ")   

# Musterinin adı: Ahmet, Musterinin soyadı: Demiroğ , Musterinin yaşı: 30  
print(f"Musterinin adı: {musteri_2.name}, Musterinin soyadı: {musteri_2.lastname} , Musterinin yaşı: {musteri_2.age} ")

# Musterinin adı: Engin, Musterinin soyadı: Demiroğ , Musterinin yaşı: 32
print(f"Musterinin adı: {musteri_3.name}, Musterinin soyadı: {musteri_3.lastname} , Musterinin yaşı: {musteri_3.age} ")
        