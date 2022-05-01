import math

def toplama(a,b):
    print(a+b)


def cikarma(a,b):
    print(a-b)


def carpma(a,b):
    print(a*b)


def bolme(a,b):
    x = (a / b)
    print("{0:.5f}".format(x)) #sonucu x'e atıp virgülden sonraki 5 hanesini yazdırmak için

print("Lütfen yapmak istediğiniz işlemi yazın:")

secim = input("Seçenekler: toplama, çıkarma, çarpma, bölme -> ")
print(secim)
a = int(input("İlk sayı: "))
b = int(input("İkinci sayı: "))

if secim == "toplama":
    toplama(a,b)
elif secim == "çıkarma":
    cikarma(a,b)
elif secim == "çarpma":
    carpma(a,b)
elif secim == "bölme":
    bolme(a,b)
else:
    print("Hatalı giriş yaptınız.")
