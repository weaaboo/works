s1 = int(input("Введите длину первой стороны: "))
s2 = int(input("Введите длину второй стороны: "))
s3 = int(input("Введите длину третьей стороны: "))
s = (s1 + s2 + s3) / 2
area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
print("Площадь треугольника равна: ", area)
