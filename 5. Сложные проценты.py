a = float(input("Введите сумму первоначального депозита: "))
b = 0.04 * a + a
c = 0.04 * b + b
d = 0.04 * c + c
print("Сумма на счету в конце 1 года: ", "%.2f" % b, "Руб.")
print("Сумма на счету в конце 2 года: ", "%.2f" % c, "Руб.")
print("Сумма на счету в конце 3 года: ", "%.2f" % d, "Руб.")
