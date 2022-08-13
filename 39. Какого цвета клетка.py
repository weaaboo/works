a = input("Введите координаты клетки на шахматном поле: ")

b = False
if a[0] == "a" or a[0] == "c" or a[0] == "e" or a[0] == "g":
    b = True

if int(a[1]) % 2 == 0 and b == True or int(a[1]) % 2 != 0 and b != True:
    print("Клетка белая")
else:
    print("Клетка чёрная")

