# Задача 1 Цикл for + итерация:
# Дан список: fruits = ["яблоко", "банан", "апельсин"]
# Выведи каждый элемент списка с новой строки
# fruits = ["яблоко", "банан", "апельсин"]
# for fruit in fruits:
#     print(fruit)



# Задача 2 Функция range:
# Используя range, выведи числа от 5 до 10 включительно
# for number in range(5,11):
#     print(number)



# Задача 3 Цикл while:
# Выводи числа от 1 до 3, используя while
# count = 0
# while count < 3:
#     print(f"Счетчик = {count}")
#     count += 1



# Задача 4 Оператор break:
# Перебирай числа от 1 до 10, но останови цикл (break), если встретишь 5
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)
#     if num == 5:
#         break



# Задача 5  (Цикл for + range):
# Используя range, выведи все чётные числа от 2 до 20 включительно.
# Подсказка: шаг range может быть отрицательным.

# for number in range(2,21,2):
#     print(number)



# Задача 6
# Бесконечный цикл: while True.
# Проси пользователя ввести число (input),
# и выходи из цикла (break), если число равно 0.
# Иначе — выводи "Число: <введённое_число>".


while True: # Бесконечный цикл
    answer = int(input("Введите число: ")) # Запрашиваем ввод
    if answer == 0: # Если ответ "0", прерываем цикл
        break
    else:
        print(f"Число: {answer} ")