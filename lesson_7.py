# Задача 1  Контекстный менеджер with
# Создай файл example.txt и запиши в него строку: "Hello, World!"

# with open("example.txt", "w") as file:
#     file.write("Hello, World!") # Записываем строку в файл



# Задача 2 Чтение файла
# Прочитай содержимое файла data.txt и выведи его построчно

# with open("example.txt", "r") as file:
#     for line in file:      # Читаем файл построчно
#          print(line)


# Задача 3 Добавление в файл
# Добавь строку "New line" в конец файла notes.txt (без перезаписи!)

# with open("example.txt", "a") as file:
#     file.write("News line")

# Задача 4 (Комбинированная):
# 1. Создай файл numbers.txt
# 2. Запиши в него числа от 1 до 5 (каждое с новой строки)
# 3. Прочитай файл и выведи сумму этих чисел

with open("example.txt", "w") as file:
    file.write("1 \n2 \n3 \n4 \n5") # Записываем строку в файл

total = 0                               # сделал ИИ
with open("example.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print("Сумма:", total)