# Задача 1 Создание и вызов функций
# Создай функцию `greet()`, которая выводит "Привет, мир!"
from itertools import count


# def greet():
#     print("Привет, мир!")
# greet()




# Задача 2  Аргументы функций
# Напиши функцию `multiply(a, b)`, которая возвращает произведение двух чисел

# def multiply(a, b):
#     return a * b
# result = multiply(3,4)
# print(result)




# Задача 3  Аргументы с дефолтными значениями
# Создай функцию `welcome(name="Гость")`, которая возвращает "Привет, <name>!"

# def welcome(name="Гость"):
#     print(f"Привет, {name}")
# welcome()



# Задача 4  Декораторы
# Напиши декоратор `@repeat(n)`, который вызывает функцию `n` раз
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):  # Цикл для повтора                # Сделал ИИ
#                 func(*args, **kwargs)  # Вызов функции
#         return wrapper
#     return decorator
#
# Применение:
# @repeat(3)
# def say_hello():
#     print("Привет!")
#
# say_hello()  # Выведет "Привет!" 3 раза




# Задача 5  (Возвращение данных из функций):
# Напиши функцию `is_even(num)`, которая возвращает `True`, если число чётное, и `False` — если нет.
# Пример вызова:
# print(is_even(4))  # Должно вернуть True
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(4))  # True