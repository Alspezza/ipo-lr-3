day = int(input("Введите дату:")) #ввод даты и месяца
month = int(input("Введите месяц:")) 
if month == 12 and day >= 1 and day <= 31:    #нахождение времени года
 print("Зима")
elif month == 1 and day >= 1 and day <= 31:
 print("Зима")
elif month == 2 and day >= 1 and day <= 28:
 print("Зима")
elif month == 3 and day >= 1 and day <= 31:
 print("Весна")
elif month == 4 and day >= 1 and day <= 30:
 print("Весна")
elif month == 5 and day >= 1 and day <= 31:
 print("Весна")
elif month == 6 and day >= 1 and day <= 30:
 print("Лето")
elif month == 7 and day >= 1 and day <= 31:
 print("Лето")
elif month == 8 and day >= 1 and day <= 31:
 print("Лето")
elif month == 9 and day >= 1 and day <= 30:
 print("Осень")
elif month == 10 and day >= 1 and day <= 31:
 print("Осень")
elif month == 11 and day >= 1 and day <= 30:
 print("Осень")
else :
 print("Некорректно введена дата или месяц")
