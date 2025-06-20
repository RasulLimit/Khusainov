# Задача 1 – Доступ к символам
# Дана строка: text = "Автоматизация"
# 1. Выведите первый символ строки
# 2. Выведите последний символ строки
# 3. Выведите символ с индексом 5

# text = "Автоматизация"
# second_char = text[0]
# end_char = text[-1]
# center_char = text[5]
# print(second_char)
# print(end_char)
# print(center_char)



# Задача 2 – Срезы
# Дана строка: text = "Программирование"
# Выведите подстроку с 3-го по 7-й символ включительно
# Напоминание: индексы начинаются с 0, срез [start:end] не включает end
# Подсказка:
# Для среза используйте text[3:8] (так как end не включается).
# Решите и отправьте ваш код. Укажу на ошибки, если они будут!

# text = "Программирование"
# text_1 = text[3:8]
# print(text_1)



# Задача 3 – F-строки
# Даны: name = "Алексей", age = 25
# Создайте строку вида: "Меня зовут Алексей, мне 25 лет"
# используя f-строку
# name = "Алексей"
# age = 25
# message = f"Меня зовут {name}, мне {age} лет"
# print(message)




# Задача 4 – Базовые методы строк
# Дана строка: text = "  робототехника  "
# 1. Удалите пробелы в начале и конце строки
# 2. Переведите строку в верхний регистр
# 3. Выведите результат

# text = "  робототехника  "
# print(text.strip())
# print(text.strip().upper())




# Задача 5 – Конкатенация строк
# Дано: part1 = "Авто", part2 = "матизация"
# Создайте новую строку из part1 и part2:
# 1. Через оператор +
# 2. Через метод .join()
# Выведите оба варианта

# part1 = "Авто"
# part2 = "матизация"
# part3 = part1 + part2
# part4 = "".join([part1, part2])
# print(part3)
# print(part4)




# Задача 6 – Получение длины строки
# Дана строка: text = "Пайтон"
# 1. Выведите её длину
# 2. Выведите длину строки после добавления к ней "3.11" (через пробел)
# Формат: len(text)

# text = "Пайтон"
# text_len = text + " 3.11"
# print(len(text))
# print(len(text_len))    # ???вот тут вопрос??? почему не считает "."??? Точнее ИИ утверждает, что ответ должен быть 6 и 10



# Задача 7 – Методы строк (продолжение)
# Дана строка: text = "Hello, world!"
# 1. Замените "world" на "Python"
# 2. Переведите строку в нижний регистр
# 3. Выведите результат

# text = "Hello, world!"
# text = text.replace("world", "Python").lower()
# print(text)




# Задача 8 – Спецсимволы в строках
# Дано: name = "Анна", age = 25
# Создайте строку: "Имя:\tАнна\nВозраст:\t25"
# и выведите ее (используйте \t и \n)

# name = "Анна"
# age = 25
# result = f"Имя:\t{name}\nВозраст: \t{age}"
# print(result)



# Задача 9 - Методы строк (продолжение)
# Дана строка: text = "!!Пайтон!!"
# 1. Удалите восклицательные знаки с обоих концов
# 2. Замените "ай" на "айт"
# 3. Выведите результат

# Дана строка: text = "!!Пайтон!!"
# 1. Удалите восклицательные знаки с обоих концов
# 2. Замените "ай" на "айт" (если есть)
# 3. Добавьте "3.10" в конец строки через пробел
# 4. Выведите результат

# text = "!!Пайтон!!"
# print(text.strip("!").replace("ай", "айт") + " 3.10")



# Задача 10 – Комбинирование методов
# Дана строка: text = "  Hello, World!  "
# 1. Удалите пробелы в начале и конце
# 2. Переведите в нижний регистр
# 3. Замените "world" на "python"
# 4. Выведите результат

# text = "  Hello, World!  "
# print(text.strip().lower().replace("world", "python"))