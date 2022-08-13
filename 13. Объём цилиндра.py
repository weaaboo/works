import math
a = int(input("Введите радиус цилиндра: "))
b = int(input("Введите высоту цилиндра: "))
c = math.pi * a * a * b
d = "%.1f" % c
print ("Объём цилиндра равен", d)
