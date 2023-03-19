class Human:
    def __init__(self,name):
        self.name = name
        print("Bir Human instance üretildi.")

    def __str__(self):
        return f"STR fonksiyonu çalıştı ve adı: {self.name}"

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")

    def walk(self):
        print(f"{self.name} is walking")

# instance -> örnek
# def __init kısmı Human classından nesne üretirken ilk o çalışır
# Human() dediğimizde classı başlat 
human = Human("Enes")
human.talk("Merhaba")

human1 = Human("Faruk")
human.talk("Selam")
human1.walk()
