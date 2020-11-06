# Henüz bitmedi (çünkü floatlarla çalışmıyor)

print("\nProgramı kapatmak için operatör girmek yerine '?' (soru işareti) girmeniz yeterlidir!!\n")
while True:
    s1 = input("İlk sayıyı giriniz: ")
    s2 = input("İkinci sayıyı giriniz: ")
    if s1.isdigit() == True and s2.isdigit() == True:
        islem = input("İstediğiniz işleme göre '+,-,*,/' operatörlerinden birini giriniz: ")
        if islem == "+":
            sonuc = float(s1)+float(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "-":
            sonuc = float(s1) - float(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "/":
            sonuc = float(s1) / float(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "*":
            sonuc = float(s1) * float(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "?":
            exit()
        else:
            print("Bir işlem operatörü girmediniz!!\n")
    else:
        print("Lütfen sayı girişi yapınız!!\n")
        
