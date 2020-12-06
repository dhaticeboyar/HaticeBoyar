git remote add origin https://github.com/dhaticeboyar/HaticeBoyar.git
git branch -M main
git push -u origin main




#Sözlük içine bir öğrencinin ihtiyacımız olan tüm verilerini key-value çiftleri şeklinde tanımladım.
student1 = {
    "name" : "yoda" ,
    "surname" : "master" ,
    "midterm" : 70 ,
    "final" : 48 ,
    "project" : 55 ,
}

#3 sayısını variableye atadım.İlerideki while bloğunda 3 hakkı temsil edecek.
number_of_trying = 3

#Bu while bloğunda kullanıcının name ve surname bilgilerini doğru girip girmediğini sınadım.
#"Welcome!" stringini görmek için lütfen yoda ve master şeklinde giriş yapınız.
while True :

    name = student1["name"]
    surname = student1["surname"]

    name1 = input("Please,tell me your name: ")
    name1 = name1.lower().strip()
    surname1 = input("Please,tell me your surname: ")
    surname1 = surname1.lower().strip()

    if (name1 == name) and (surname1 == surname) :
        print("Welcome!")
        break

    else:
        print("Name or surname is wrong.")
        number_of_trying -= 1
        
    if number_of_trying == 0 :
        print("Please,try again later!")
        quit()

#Hata mesajını yayınlamak için bir fonksiyon tanımladım.
def failure_giving():
    failure = "You failed in class!"
    return failure  

#Boş bir liste tanımladım,ilerideki for bloğunda kullanıcıdan alınan girdi burada depolanacak
users_courses = []

#Varsayılan dersleri tanımladım.Bunlardan biri seçilmeli ki kullanıcı dersten kalmasın.
default_courses = ["algebra","biology","calculus","english","law","science","turkish"]

#Varsayılan ders listesini none değeri almadan tekrar tekrar kullanmak için bir fonksiyon tanımladım.
def course_list():
    global default_courses
    
    return default_courses

print("You must choose minimum 3 courses to graduate!")
print("You must choose one of these! ")
print(course_list())

#Kullanıcıdan 5 adet ders girdisi alınacak.Çünkü kullanıcı max 5 ders seçebilmeli demiştik.
for i in range(0,5):
    
    course_choose = input("Which course do you want to take? : ")
    course_choose = course_choose.lower()
    users_courses.append(course_choose)
    if "" in users_courses :
        users_courses.remove("")
    
#Eğer 3'ten az ders girilirse kullanıcı dersten kalacak.
if len(users_courses) < 3 :
    print(failure_giving())

#Kullanıcı varsayılan derslerden birini girmez ise sistem kapanacak çünkü o dersler varsayılan dersler mutlaka seçilmeli.

if not ("algebra" or "biology" or "calculus" or "english" or "law" or "science" or "turkish") in users_courses :
    print("You don't choose necesarry courses!")
    print("If you think we made a mistake ,try again later!")
    quit()
else:
    print("You choose these courses: {}".format(users_courses))

#Kullanıcıdan sınav dersini seçmesini istedik.
exam_course = input("Which one do you want to take exam? : ")
exam_course = exam_course.lower()

#Eğer seçtiği ders daha önce seçtiği dersler arasında yoksa uyarı mesajı yazdırıp sistemden çıktık.
#Eğer seçtiği ders listede varsa notlar sistemden alınıyor dedik ve devam ettik
if not exam_course in users_courses :
    print("There isn't in your courses!")
    print("Please,try again later!")
    quit()
else:
    print("Your grades are taken from the system...")

#En başta kullanıcının bütün bilgilerini listede tutmuştuk.Şimdi onlardan midterm,final,project olanı yani notlarla ilgili olanı aldık.
midterm = student1["midterm"]
final = student1["final"]
project = student1 ["project"]
print("Your midterm grade is : {}".format(midterm))
print("Your final grade is : {}".format(final))
print("Your project grade is : {}".format(project))

#Ortalamasını aldık.
avarage_of_grades = (midterm * 0.3 ) + (final * 0.5 ) + (project * 0.2)

#Ortalamaya göre notları harf notuna çevirdik ; eğer geçtikse harf notunu,kaldıysa uyarı mesajını yazdırdık.    
if avarage_of_grades > 90 :
    print("Your grades is : {}".format(avarage_of_grades))
    print("You take : AA ")
        
elif 70 < avarage_of_grades < 90 :
    print("Your grades is : {}".format(avarage_of_grades))
    print("You take : BB ")  
        
elif 50 < avarage_of_grades < 70 :
    print("Your grades is : {}".format(avarage_of_grades))
    print("You take : CC ")
        
elif 30 < avarage_of_grades < 50 :
    print("Your grades is : {}".format(avarage_of_grades))
    print("You take : DD ")
        
elif avarage_of_grades < 30 :
    print("Your grades is : {}".format(avarage_of_grades))
    print("You take : FF ")
    print(failure_giving())
        




    

 





          
    
   
        


            
            

            
           
   
    
    
        

       
        
      
    