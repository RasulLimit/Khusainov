# Задача 1 Создание класса
# Создай класс `Car` без атрибутов и методов
from tkinter.font import names


class Car:
    NAME_CAR = "BMW"
my_car = Car()
print(my_car.NAME_CAR)



# Задача 2 Конструктор __init__
# Добавь классу `Robot` конструктор с параметрами `name` и `model`

class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

autobot = Robot
print(autobot.__name__)             #Почему если тут указть __model__ то ничего не показывает, но если указать,
                                    # __name__ выведет Robot

technology = Robot("р.Валера", "р.Олег")                    #Эта версия правильнее
print(f"Роботы: {technology.name}, and {technology.model}")

# Задача 3  Методы класса
# Создай класс `Calculator` с методом `add(a, b)`, возвращающим сумму

class Calculator:
    def add(self, a, b):  # Обычный метод
        return a + b

calc = Calculator()
print(calc.add(3, 4))  # Выведет 7


# Задача 4  Работа с объектами
# Создай объект класса `Book` с атрибутами `title` и `author`, затем выведи их

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

my_book = Book("Введение", "А.С. Пушкин")
print(f"Книга: {my_book.title}, автор: {my_book.author}")

# Задача 5 (Комбинированная):
# Создай класс `Student`:
# 1. С конструктором, принимающим `name` (обязательный) и `grade` (по умолчанию "A")
# 2. С методом `upgrade()`, который повышает оценку на 1 уровень (A → B → C)
# 3. Создай объект и вызови метод

# Пример:
# student = Student("Иван", "B")
# student.upgrade()  # Должно стать "C"

# class Student:
#     def __init__(self,name, grade="A"):
#         self.name = name
#         self.grade = grade
#
#     def grades(self, ["A", "B", "C"]):
#
#     def upgrade:
#         grades.index(self.grade)
#         if current_index < len(grades) - 1:
#              self.grade = grades[current_index + 1]
#
# student = Student("Иван", "B")
# student.upgrade()  # Оценка станет "C"
# itog = Student.grades.index()
# print(student.grade)

#
# class Student:
#     grades = ["A", "B", "C"]  # Добавь это
#
#     def __init__(self, name, grade="1"):
#         self.name = name
#         self.grade = grade
#
#     def upgrade(self):  # Исправь название и добавь self
#         current_index = "A"  # Найди индекс текущей оценки
#         if current_index < len(self.grades) - 1:  # Если это не "C"
#             self.grade = self.grades[current_index + 1]  # Повышаем оценку
#         current_index = self.grades.index(self.grade)  # Возвращает позицию оценки в списке
# student = Student("Иван", "B")
# student.upgrade()  # Должно стать "C"

class Student:
    grades = ["A", "B", "C"]  # Список возможных оценок

    def __init__(self, name, grade="A"):
        self.name = name
        self.grade = grade

    def upgrade(self):
        current_index = self.grades.index(self.grade)  # Получаем индекс текущей оценки
        if current_index < len(self.grades) - 1:  # Если это не последняя оценка
            self.grade = self.grades[current_index + 1]  # Повышаем оценку


# Проверка работы:
student = Student("Иван", "A")
print(f"Начальная оценка: {student.grade}")  # B
student.upgrade()
print(f"Новая оценка: {student.grade}")  # C