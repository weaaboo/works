import math
s = int(input("Введите значение длины стороны: "))
n = int(input("Введите количество сторон: "))
area = n * s * s / 4 * math.tan(math.pi / n)
print(area)

