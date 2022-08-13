a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

d = [a,b,c]
d1 = min(d)
d2 = max(d)
d3 = a + b + c - d1 - d2

print(d1, d3, d2)
