# Bu kadar uzun gözükmesinin sebebi, başka bir türlü float sayıları da hesap makinesine dahil edememem oldu.
print("\nProgramı kapatmak için operatör girmek yerine '?' (soru işareti) girmeniz yeterlidir!!\n")
while True:
    ondalik_s1 = 0 # Float tipi s1 için (Nokta girildiyse birden fazla girilip girilmediğini kontrol eder)
    ondalik_s2 = 0 # Float tipi s2 için (Nokta girildiyse birden fazla girilip girilmediğini kontrol eder)
    s1 = input("İlk sayıyı giriniz: ")
    s2 = input("İkinci sayıyı giriniz: ")
    # -------- Float'ları da dahil edebilmek için diğer '#' işaretine kadar olan işlemi yapıyorum --------
    for x in range(0,len(s1)):
        if len(s1) > 2 and s1[x] == ".": # Tek başına nokta girilmesi durumunu kontrol ediyor.
            ondalik_s1 += 1
    if ondalik_s1 == 1: # Girdi tek bir nokta barındırıyorsa o ondalıklı bir sayıdır
        s1 = float(s1)
    for x in range(0,len(s2)):
        if len(s2) > 2 and s2[x] == ".": # Tek başına nokta girilmesi durumunu kontrol ediyor.
            ondalik_s2 += 1
    if ondalik_s2 == 1: # Girdi tek bir nokta barındırıyorsa o ondalıklı bir sayıdır.
        s2 = float(s2)
    # -------------------------------- İşlemlerin sonu --------------------------------
    if (type(s1) == float or type(s2) == float): # Sayının float olup olmaması şartına öncelik veriyorum, çünkü önce isdigit() şartına gelen bir float sisteme hata verdiriyor!
        islem = input("İstediğiniz işleme göre '+,-,*,/' operatörlerinden birini giriniz: ")
        if islem == "+":
            sonuc = float(s1) + float(s2)
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
            exit() # Bu komutu klavyeden otomatik olarak enter'a basarak desteklemek isterdim ancak onun için standart modüller içinde bulunan bir komut yokmuş.
        else:
            print("Bir işlem operatörü girmediniz!!\n")
    elif (s1.isdigit() == True and s2.isdigit() == True): # float tipi sayı girildiğinde bu şartı kontrol edip programı her seferinde durduğu için yukarıdakinden ayırmak durumunda kaldım.
        islem = input("İstediğiniz işleme göre '+,-,*,/' operatörlerinden birini giriniz: ")
        if islem == "+":
            sonuc = int(s1) + int(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "-":
            sonuc = int(s1) - int(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "/":
            sonuc = float(s1) / float(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "*":
            sonuc = int(s1) * int(s2)
            print("İşlemin sonucu: ",sonuc,"\n")
        elif islem == "?":
            exit() # Bu komutu klavyeden otomatik olarak enter'a basarak desteklemek isterdim ancak onun için standart modüller içinde bulunan bir komut yokmuş.
        else:
            print("Bir işlem operatörü girmediniz!!\n")
    else:
        print("Lütfen sayı girişi yapınız!!\n")
        
