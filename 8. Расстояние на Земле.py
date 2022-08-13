import math
t1 = math.radians(float(input("Введите широту первой точки: ")))
g1 = math.radians(float(input("Введите долготу первой точки: ")))
t2 = math.radians(float(input("Введите широту второй точки: ")))
g2 = math.radians(float(input("Введите долготу второй точки: ")))
distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print("Дистанция между точками равна ", distance, "Км")
