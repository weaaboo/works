a = input("Введите название месяца: ")
b = int(input("Введите номер дня: "))


if a == "январь" or a == "февраль" or a == "декабрь" and b > 20 and b <= 31 or a == "март" and b > 0 and b < 20:
    print("Это зимний день")
    
elif a == "апрель" or a == "май" or a == "март" and b > 19 and b <= 31 or a == "июнь" and b > 0 and b < 21:
    print("Это весенний день")
    
elif a == "июль" or a == "август" or a == "июнь" and b > 20 and b <= 31 or a == "сентябрь" and b > 0 and b < 22:
    print("Это летний день")
    
elif a == "октябрь" or a == "ноябрь" or a == "сентябрь" and b > 21 and b <= 31 or a == "декабрь" and b > 0 and b < 21:
    print("Это зимний день")
else:
    print("Введено неверное значение")

