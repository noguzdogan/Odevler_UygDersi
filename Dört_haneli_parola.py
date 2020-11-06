# Hanelere tek tek bakarak gereksiz uzattığımın farkındayım, onu bir ara düzelticem şimdi karışık geliyor.
sifre = input("Lütfen yeni bir şifre giriniz: ")   
dogruluk = 0 # Girilen her hanenin bir rakam olup olmadığını kontrol edicek.
for x in range(0,len(sifre)): # 4 haneden az girilme ihtimaline karşın aralığı len(sifre)'yle belirtiyorum
    if sifre[x].isdigit() == True:
        dogruluk+=1 # Girilen hane bir rakamsa o hane şifre elemanı olmak için doğru bir karakter oluyor.
while len(sifre) != 4 or dogruluk != 4: # İstenmeyen durumu kontrol ediyor.
    sifre = input("\nGirdiğiniz şifre istenmeyen karakterler barındırıyor.\nLütfen sadece rakamlardan oluşan 4 haneli bir şifre giriniz: ")
    dogruluk = 0
    for x in range(0,4): #Yukarıdaki döngünün aynısı (rekülsif fonksiyona da ekleyebilirdim ama sanırım henüz işlemedik)
        if sifre[x].isdigit() == True:
            dogruluk+=1 
print("Yeni şifreniz: ",sifre)
