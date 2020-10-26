# Bulabildiğim kadarıyla 3 farklı tipte satır kaydırma yapabiliriz.
# (ama print() kullanmaksızın nasıl yapabileceğimi bulamadım)

# 1: \n ifadesini direkt kullanarak
print("First Line\nSecond Line")

# 2: Son satırı 'end =' ile belirleyerek ('end='in hemen sağına virgül atıp yeni satır ekleyemiyorum)
print("\n\n") # sadece satırlar arasına mesafe koymak için ekledim
print("1st Line", end = "\n2nd Line")

# 3: Satırları 'sep =' ifadesiyle ayırıp ona '\n' değerini atayarak (öncekine göre daha çok satır ayırabiliyorum)
print("\n\n")
print("İlk Satır","İkinci Satır","Üçüncü Satır", sep="\n")
