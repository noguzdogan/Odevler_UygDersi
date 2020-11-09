sifre = input("Lütfen yeni bir şifre giriniz: ")
while len(sifre) != 4 or sifre.isdigit() != True: # İstenmeyen durumu kontrol ediyor.
    sifre = input("\nGirdiğiniz şifre istenmeyen karakterler barındırıyor.\nLütfen sadece rakamlardan oluşan 4 haneli bir şifre giriniz: ")
print("Yeni şifreniz: ",sifre)
