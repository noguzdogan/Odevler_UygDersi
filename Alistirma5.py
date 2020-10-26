print("4 basamaklı palindromik sayılar şunlardır:\n")
for x in range(1000,9999):
    strduz = str(x)
    strters = strduz[::-1]
    if (strduz == strters):
        print(strduz,end=" ")
