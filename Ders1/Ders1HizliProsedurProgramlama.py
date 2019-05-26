import random

#metot oluşturma ve çağırma
def topla(sayi1, sayi2):
    return sayi1 + sayi2


sonuc = topla(1, 4)
print(sonuc)

x = random.randint(1, 6)
print(x)


def fonsiyonAdi():
    print("Fonksiyon adı çağrıldı")

fonsiyonAdi()



#okuma/yazma işlemi konsolda

girilenYazi = input("Bir şey yazar mısın? ")
print("Yazılan yazı : ", girilenYazi)


#aritmatik operatörler
sayi1 = 10
sayi2 = 10
topla = sayi1 + sayi2
print("Toplamı", topla)

# a += 1 demek aslında a = a + 1
# a -= 1 demek aslınad a = a - 1


ad = "Enis Kurtay"
soyad = "Yılmaz"
print(ad + soyad)
#mantıksal ifadedeler - logical

#hatalı tip dönüşümü

try:
    print(int("123asd"), type(int("123")))
    print("metin ifade"[123])
except ValueError as err:
    print("Hatalı bir şey oldu, sebebi : ", err)
except IndexError as err:
    print("Dizi aşımı oldu", err)




for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter, "ünlü")
    else:
        print(letter, "ünsüz")


sayi = 1
while(sayi < 11):
    print(sayi)
    sayi = sayi + 1


sinavSonucu = 65
if(sinavSonucu >= 50):
    print("Geçti")
else:
    print("Kaldı")

if(sinavSonucu>= 0 and sinavSonucu <= 25):
    print("Kaldı")
elif(sinavSonucu >= 26 and sinavSonucu <= 49):
    print("Ortalamaya kaldı")
elif(sinavSonucu >= 50 and sinavSonucu <= 70):
    print("iyi geçti")
elif(sinavSonucu >= 71 and sinavSonucu <= 85):
    print("Daha da iyi")
else:
    print("pek iyi")


a = 50
b = 10
c = 20
print(a > b)
print(a < b)
print(a == b)

print(a > b and a < c) #false
demet = ("Bakırköy", "Zeytinburnu", "Üsküdar", "Kadıköy")
print("Üsküdar" in demet)


#liste - demet - collection data types
#demet = tuple #sabit
#liste = list #değişebilir

demet = ("Bakırköy", "Zeytinburnu", "Üsküdar", "Kadıköy")
print(demet, type(demet))
print(demet[2])

liste = ["Yol 1", "Yol 2", "Yol 3", "Yol 4"]
liste.append("Yol 5")
print(len(liste))
print(liste, type(liste))
print(liste[2])

#nesne referansları - object references
route = 866
print(route, type(route))

route = "North"
print(route, type(route))


x = "Kırmızı"
y = "Beyaz"
z = "Mavi"

print(x, y, z)

y = "Siyah"
print(x, y, z)

y = z
print(x, y, z)

z = "Mor" #z'yi değiştirirsem, y de değişir mi?
print(x, y, z)

#veri tipleri - datatypes
"python dersleri" #15 karakteri
print("python dersleri"[0])
print("python dersleri"[5])
print("python dersleri"[14])

#dizinin veya metinin uzunluğu - 1
print("python dersleri"[len("python dersleri") - 1])
print(len("python dersleri"))


print("python dersleri"[0])
print("python dersleri"[-1])

"123"
print(int("123"), type(int("123")))
#tip dönüşümleri int(degiskenAdini), str(degiskenAdi)

#hatalı tip dönüşümü
#"123a"#
#print(int("123"), type(int("123a")))
#tip dönüşümleri int(degiskenAdini), str(degiskenAdi)

print(str(123), type(str(123)))