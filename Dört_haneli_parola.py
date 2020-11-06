sifre = input("Lütfen yeni bir şifre giriniz: ")
liste = [] # Biraz gereksiz olabilir kodu sürekli değiştirirken bir ara kullanmak çok mantıklı geldi.      
dogruluk = 0 # Girilen her hanenin bir rakam olup olmadığını kontrol edicek.
for x in range(0,4): # Sadece ilk 4 hanenin rakam olup olmadığına bakıyorum çünkü while'da şart olarak len(sifre)'yi de belirttim.
    liste.append(sifre[x])
    if sifre[x].isdigit() == True:
        dogruluk+=1 # Girilen hane bir rakamsa o hane şifre elemanı olmak için doğru bir karakter oluyor.
while len(sifre) != 4 or dogruluk != 4: # İstenmeyen durumu kontrol ediyor.
    sifre = input("\nGirdiğiniz şifre istenmeyen karakterler barındırıyor.\nLütfen sadece rakamlardan oluşan 4 haneli bir şifre giriniz: ")
    liste = []
    dogruluk = 0
    for x in range(0,4): #Yukarıdaki döngünün aynısı (rekülsif fonksiyona da ekleyebilirdim ama sanırım henüz işlemedik.)
        liste.append(sifre[x])
        if sifre[x].isdigit() == True:
            dogruluk+=1 
print("Yeni şifreniz: ",sifre)
