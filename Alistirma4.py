print("3 basamaklı palindromik sayılar şunlardır:\n")
for x in range(100,999):
    strduz = str(x)
    strters = strduz[::-1]
    if (strduz == strters):
        print(strduz,end=" ")
