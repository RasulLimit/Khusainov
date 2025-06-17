# Задача 1
# Создай:
# 1. Базовый класс `Animal` с методом `eat()` (выводит "Я ем")
# 2. Дочерний класс `Dog`, который наследует `Animal` и добавляет метод `bark()` ("Гав!")
# 3. Создай объект `Dog` и вызови оба метода

# class Animal:
#     def eat(self):
#         return "Я ем"
# class Dog(Animal):
#     def __init__(self, my_dog):
#         self.my_dog = my_dog
#     def bark(self):
#         return (f"Моя собака {self.my_dog} делает: Гав!")
# my_dog = Dog("Овчарка")

# print(my_dog.eat())
# print(my_dog.bark())


# Задача 2
# 1. Создайте базовый класс `Vehicle` с методом `move()` ("Транспорт движется")
# 2. Создайте дочерний `Boat` с дополнительным методом `swim()`
# 3. Создайте дочерний `Car` с методом `drive()`
# 4. Создайте объекты каждого класса и вызовите их методы

class Vehicle:
    def move(self):
        return ("Транспорт движется")

class Boat(Vehicle):
    def swim(self):
        return ("Лодка плывет по воде")

class Car(Vehicle):
    def drive(self):
        return ("Ехать на машине в сторону заката")

transport = Vehicle()
plovec = Boat()
driver = Car()

print(transport.move())
print(plovec.move())
print(driver.drive())



# Задача 3
# 1. Создайте базовый класс `Person` с методом `walk()` ("Иду пешком")
# 2. Создайте дочерний `Runner`, который:
#    - Добавляет метод `run()` ("Бегу быстро!")
#    - Переопределяет `walk()` ("Иду спортивной ходьбой")
# 3. Продемонстрируйте разницу в поведении методов


class Person:
    def walk(self):
        return "Иду пешком"


class Runner(Person):
    def run(self):
        return "Бегу быстро"
    def walk(self):
        return "Иду спортивной ходьбой"

go = Person()
go1 = Runner()
print(go.walk())
print(go1.walk())