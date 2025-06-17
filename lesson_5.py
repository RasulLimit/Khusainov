# Задача 1 (Создание словаря)
# Создай словарь book с ключами: "title", "author", "year" и значениями: "1984", "Оруэлл", 1949


# book = {
#     "title": "1984",
#     "author": "Оруэлл",
#     "year": 1949
# }
# print(book)



# Задача 2 (Доступ по ключу)
# Дан словарь:
# person = {"name": "Иван", "age": 25, "city": "Москва"}
# Выведи значение возраста (age) и города (city) в формате:
# "Возраст: 25, Город: Москва"

# age = person["age"]
# city = person["city"]
# print(f" Возраст: {age}, Город: {city}")




# Задача 3:
# car = {"brand": "Toyota", "model": "Corolla", "year": 2015}
# 1. Обнови год на 2022
# 2. Добавь новый ключ "color" со значением "синий"
# 3. Выведи итоговый словарь
#
# car["year"] = 2022
# car["color"] = "синий"
# print(car)




# Задача 4 (Удаление элементов)
# student = {"name": "Анна", "age": 20, "course": "Python", "grade": "A"}
# Задание:
# 1. Удали ключ "grade" методом `del`
# 2. Удали ключ "age" методом `.pop()` с выводом удалённого значения (print)
# 3. Выведи итоговый словарь

# del student["grade"]
# age = student.pop("age")
# print(age)
# print(student)



# Задача 5 (Методы словарей)
# country = {"name": "Япония", "capital": "Токио", "population": 126_500_000}
# Задание:
# 1. Выведи список всех ключей через метод `.keys()`
# 2. Выведи список всех значений через метод `.values()`
# 3. Проверь, есть ли ключ "language" в словаре (без if), и выведи результат

# print(country.keys())
# print(country.values())
# print("language" in country)  # Выведет False



# Задача 6 (Генерация словаря)
# Создай словарь squares, где ключи — числа от 1 до 5, а значения — их квадраты
# Пример: {1: 1, 2: 4, 3: 9, ...}

# for item in range (1, 6):
#     print(item ** 2)
# squares = {x: x**2 for x in range(1, 6)}   #Это вариант от ИИ
# print(squares)

# squares = {}                               #Это вариант от ИИ
# for x in range(1, 6):
#     squares[x] = x ** 2
# print(squares)




# Задача 7 (Объединение словарей)
# Даны 2 словаря:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# Создай новый словарь, объединяющий оба (все ключи должны быть в одном словаре)
#
# new_dict = dict1.copy()  # Создаём копию первого словаря
# new_dict.update(dict2)   # Добавляем пары из второго
# print(new_dict)


# Задача 8 (Проверка значений)
# grades = {"Алексей": 5, "Мария": 4, "Иван": 3, "Ольга": 5}
# Задание:
# 1. Проверь, есть ли в словаре хотя бы одна оценка "5" (выведи True/False)
# 2. Проверь, все ли оценки >= 4 (выведи True/False)

# print(5 in grades.values())
# all_grades = all(grade >= 4 for grade in grades.values())
# print(all_grades)



# Задача 9 (Глубокое копирование)
original = {"data": [1, 2, 3], "meta": {"version": 1}}
# Задание:
# 1. Создай поверхностную копию словаря (shallow copy)
# 2. Создай глубокую копию (deep copy)
# 3. Измени список "data" в исходном словаре: original["data"].append(4)
# 4. Выведи оба скопированных словаря и объясни разницу

import copy

original = {"data": [1, 2, 3], "meta": {"version": 1}}
shallow_copy = original.copy()  # Поверхностная копия
deep_copy = copy.deepcopy(original)  # Глубокая копия

# Изменяем оригинал
original["data"].append(4)

print("Оригинал:", original)
print("Поверхностная копия:", shallow_copy)  # data изменится!
print("Глубокая копия:", deep_copy)  # data останется [1, 2, 3]