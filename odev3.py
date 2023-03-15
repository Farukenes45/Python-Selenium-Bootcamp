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
student_list = []                

def addStudent():
    name_surname = input("Eklemek istediğiniz öğrencinin adını ve soyadını girin: ")
    student_list.append(name_surname)
    print(student_list)

addStudent()
addStudent()


# ------------------------------ Öğrenci Silme (for döngüsü) ----------------------
def deleteStudent():
    name_surname = input("Silmek istediğiniz öğrencinin adını girin: ")
    for student in student_list:
        if name_surname == student:
            student_list.remove(name_surname)
            print(f"--> Silinen Öğrencinin adı: {name_surname}")
            print(f"--> Güncel Liste: {student_list}")
        else:
            print("--> Böyle bir kullanıcı bulunamadı !!")

deleteStudent()

# ------------------------------ Çoklu Öğrenci Ekleme (while döngüsü) ----------------------
def multipleAddStudent():
    quantity = int(input("Kaç adet öğrenci eklemek istersiniz ?: "))
    counter = 0
    while counter < quantity:
        name_surname =input("Eklemek istediğiniz öğrencinin adı ve soyadını girin: ")
        student_list.append(name_surname)
        #print(student_list)
        counter+=1
        
multipleAddStudent()
print(f"--> Güncel Kayıtlı Öğrenci Listesi: {student_list}")

# ---------------------------- Öğrencileri Tek Tek Yazdırma ----------------------
def printStudent():
    for registered_student in student_list:
        print(registered_student)
        # return registered_student
    
# registered_student = printStudent()
#print(registered_student)
printStudent()

# ----------------------------- Öğrenci Numarası Öğrenme ----------------------
def learnStudentNumber():
    
    name_surname = input("Numarasını öğrenmek istediğiniz öğrencinin adı ve soyadını girin: ")

    if name_surname in student_list:                                                            # aldığımız isim öğrenci listesinde var mı yokmu kontrolü yaptık
        for student in student_list:                                                            # var ise for döngüsü ile listemizi gezdik
            if name_surname == student:                                                         # girmiş olduğumuz isim bilgisi ile for döngüsündeki dönen değer eşitse
                studentNumber = student_list.index(student)                                     # ogrenci_listesindeki ogrencinin indexini alıp number isimli değişkene atadık
                print(f"--> {name_surname} isimli öğrencinin numarası: {studentNumber}")
    else:
        print("Böyle bir kullanıcı bulunamadı !!")
        print(f"Güncel Liste --> {student_list}")    

learnStudentNumber()
learnStudentNumber()
learnStudentNumber()
learnStudentNumber()

# ----------------------------- Çoklu Öğrenci Silme (for döngüsü) ----------------------
def multipleDeleteStudent():
    quantity = int(input("Listeden kaç öğrenci silmek istiyorsunuz ?:"))                        # silinecek öğrenci adetini aldık
    if quantity <= len(student_list):                                                           # adet sayısı listemizdeki sayıdan küçük veya eşitmi
        for qty in range(quantity):                                                 
            name_surname = input("Silmek istediğiniz öğrencilerin adını ve soyadını girin: ")
            if name_surname in student_list:
                student_list.remove(name_surname)
                print(f"--> Güncel Liste: {student_list} ")
    else:                                                                                       # girilen adet sayısı listedeki öğrenci sayısından fazla olamaz
        print("--> Girdiğiniz adet sayısı listedeki öğrenci sayısından fazla , tekrar deneyin")
        print(f"--> Listedeki toplam öğrenci sayısı: {len(student_list)}")

multipleDeleteStudent()