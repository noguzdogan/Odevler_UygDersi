total =0
for x in range(1000,9999):
    su_ic = str(x)
    ilk = int(su_ic[0])
    son = int(su_ic[3])
    if (ilk > son):
        total = total + 1
print("İlk rakamı son rakamından büyük olan sayıların toplam adedi: ",total)

            
