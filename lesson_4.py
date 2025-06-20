# Задача 1 – Оператор if  
# Напиши код, который проверяет значение переменной age:
# Если age больше или равно 18, вывести "Доступ разрешён".

# age = 15
# if age > 18 or age == 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")




# Задача 2 – Оператор else
# Дано: password = "qwerty123"
# Напишите условие:
# 1. Если password равен "admin", выведите "Доступ разрешён"
# 2. В остальных случаях — "Неверный пароль"
# password = "qwerty123"
# if password == "admin":
#     print("Доступ разрешен")
# else:
#     print("Неверный пароль")



# Задача 2.1 Напиши код, который проверяет значение переменной number:
# Если number больше 10, вывести "Больше 10"
# Если number равно 10, вывести "Равно 10"
# В остальных случаях — "Меньше 10"

# number = 7
# if number > 10:
#     print("Больше 10")
# elif number == 10:
#     print("Равно 10")
# else:
#     print("Меньше 10")



# Задача 3 (Логические операции and, or)
# Напиши код, который проверяет значение переменной x:
# Если x находится в диапазоне от 5 до 15 включительно, вывести "В диапазоне"
# Иначе — "Вне диапазона"

# x = 14
# if x > 5 and x < 15:
#     print("В диапазоне")
# else: print("Вне диапазона")



# Задача 4
# temperature = 28
# Замени условие ниже на тернарный оператор
# if temperature > 25:
#     print("Жарко")
# else:
#     print("Прохладно")


# temperature = 28
# result = "Жарко" if (temperature > 25) else "Прохладно"
# print(result)



# Задача 5
# num = 7
# Напиши код, который проверяет:
# 1. Является ли num чётным (even) или нечётным (odd)
# 2. Если чётное — вывести "Чётное"
# 3. Если нечётное — проверить, больше ли оно 5, и вывести:
#    - "Нечётное и больше 5" (если да)
#    - "Нечётное и 5 или меньше" (если нет)

# num = 7
# if num % 2 == 0:
#     print("Чётное")
# else:
#     if num > 5:
#         print("Нечётное и больше 5")
#     else:
#         print("Нечётное и 5 или меньше")



# Задача 8 (Комбинированные логические условия)
# Напиши код, который проверяет переменную score (баллы):
# Если score от 80 до 100 → "Отлично"
# Если от 50 до 79 → "Хорошо"
# Если от 20 до 49 → "Удовлетворительно"
# Если меньше 20 → "Неудовлетворительно"

# score = 100
# if score >= 80 and score <= 100:
#     print("Отлично")
# elif score >= 50 and score <= 79:
#     print("Хорошо")
# elif score >= 20 and score <= 49:
#     print("Удовлетворительно")
# elif score < 20:
#     print("Неудовлетворительно")



# Задача 9
# weather = "дождь"
# temperature = 14
# Напиши код, который выводит:
# "Зонт нужен" — если weather == "дождь" И temperature > 0
# "Зонт не нужен" — во всех остальных случаях
# Используй тернарный оператор и логическое and.

# weather = "дождь"
# temperature = 14
# if weather == "дождь" and temperature > 0:
#     print("Зонт нужен")
# else:
#     print("Зонт не нужен")



# Задача 10 (not + вложенные условия):
# Напиши код, который проверяет:
# 1. Если сегодня не выходной (not is_weekend) И время >= 22, вывести "Пора спать!"
# 2. Если сегодня выходной, но время >= 23, вывести "Можно не спать, но уже поздно"
# 3. В остальных случаях — "Бодрствуем"

# is_weekend = True
# time = 23
# if not is_weekend and time >= 22:
#     print("Пора спать")
# elif is_weekend and time >= 23:
#     print("Можно не спать, но уже поздно")
# else: print("Бодрствуем")