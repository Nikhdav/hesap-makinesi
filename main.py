import math


def hesap_makinesi():
    print("=== Hesap Makinesi ===")
    print("İşlemler: +  -  *  /  ^  %  √")
    print("Çıkmak için 'q' yazabilirsiniz.")

    while True:
        islem = input("\nİşlemi seç (+, -, *, /, ^, %, √, q): ")

        if islem == "q":
            print("Program kapatıldı.")
            break

        # Karekök işlemi tek sayı alır
        if islem == "√":
            sayi = float(input("Sayiyi gir: "))
            if sayi >= 0:
                sonuc = math.sqrt(sayi)
                print(f"Sonuç: {sonuc}")
            else:
                print("Negatif sayının karekökü alınamaz!")
            continue

        # Diğer işlemler iki sayı alır
        sayi1 = float(input("1. sayıyı gir: "))
        sayi2 = float(input("2. sayıyı gir: "))

        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
            else:
                print("Hata: Sıfıra bölme yapılamaz!")
                continue
        elif islem == "^":
            sonuc = sayi1**sayi2
        elif islem == "%":
            sonuc = sayi1 % sayi2
        else:
            print("Geçersiz işlem seçtin!")
            continue

        print(f"Sonuç: {sonuc}")


hesap_makinesi()
