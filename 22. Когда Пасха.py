import math

year = int(input("Введите год: "))

a = year % 19
b = math.floor(year / 100)
c = year % 100
d = math.floor(b / 4)
e = b % 4
f = math.floor((b + 8) / 25)
g = math.floor((b - f + 1) / 3)
h = (19 * a + b - d - g + 15) % 30
i = math.floor(c / 4)
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = math.floor((a + 11 * h + 22 * l) / 451)

month = (h + l + 7 * m + 114) / 31
day = 1 + (h + 1 - 7 * m + 114) % 31

print("В этом году Пасха приходится на", \
    "%02d.%02d." % (month, day))

input("Чтобы завершить программу нажмите кнопку ввода")
