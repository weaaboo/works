w = int(input("Введите ваш вес в килограммах: "))
hh = int(input("Введите ваш рост в сантиметрах: "))
h = hh / 100
bmi = w / (h ** 2)
print("Ваш ИМТ составляет", "%.2f" % bmi)

