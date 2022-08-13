schot = int(input("Сколько рублей составляет ваш счёт в ресторане?: "))
nalog = 0.12*schot
chaevie = 0.18*schot
itog = schot + nalog + chaevie
print ("Налог составляет: ", "%.2f" % nalog, "рублей")
print ("Чаевые: ", "%.2f" % chaevie, "рублей")
print ("Итого: ", "%.2f" % itog, "рублей")
