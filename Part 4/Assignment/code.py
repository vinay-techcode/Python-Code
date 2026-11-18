# Q. 1?
# class BankAccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount Deposited")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Amount Withdrawn")
#         else:
#             print("Insufficient Balance")

#     def check_balance(self):
#         print("Current Balance:", self.balance)


# acc1 = BankAccount(123456, "Vinay", 10000)

# acc1.deposit(2000)
# acc1.check_balance()

# acc1.withdraw(3000)
# acc1.check_balance()

# Q. 2?
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.reviews = []

#     def add_review(self, review):
#         self.reviews.append(review) 

#     def count_reviews(self):
#           print(len(self.reviews)) 

#     def display_reviews(self):
#          for review in self.reviews:
#               print(review) 

# book1 = Book("Python Basics", "Vinay")

# book1.add_review("very good")
# book1.add_review("Exellent")
# book1.add_review("Easy to Understand")

# print(book1.title)
# print(book1.author)

# book1.count_reviews()
# book1.display_reviews()

# Q. 3?
# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks

#     def get_name(self):
#         return self.__name

#     def set_name(self, new_name):
#         if (new_name != ""):
#             self.__name = new_name
#         else:
#             print("Name can't be empty")

#     def get_roll_no(self):
#         return self.__roll_no

#     def set_roll_no(self, roll_no):
#         if(roll_no >= 1 and roll_no <= 100):
#             self.__roll_no = roll_no
#             print("Roll no is valid")

#         else:
#              print("Invalid roll no")

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#        if marks >= 0:
#           self.__marks = marks
#           print("Positive Marks")

#        else:
#         print("Negative Marks")

# s1 = Student("vinay", 66, 99)

# print(s1.get_name())
# print(s1.get_roll_no())
# print(s1.get_marks())

# s1.set_name("Rahul")
# s1.set_roll_no(50)
# s1.set_marks(-85)

# print(s1.get_name())
# print(s1.get_roll_no())
# print(s1.get_marks())

# Q. 4?
# class Shape:
#     def area(self):
#         print("Area of Shape")

# class Rectangle(Shape):
#     def area(self):
#         print("Area of Rectangle")

# class Triangle(Shape):
#     def area(self):
#         print("Area of Triangle")

# class Circle(Shape):
#     def area(self):
#         print("Area of Circle")

# r1 = Rectangle()
# t1 = Triangle()
# c1 = Circle()

# r1.area()
# t1.area()
# c1.area()
    
# Q. 5?
# Concept Inheritance
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#    def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc

# car1 = Car("Toyota", "Fortuner", 7)
# bike1 = Bike("Royal Enfield", "Clsssic 350", 250)

# print(car1.brand, car1.model, car1.seats)
# print(bike1.brand, bike1.model, bike1.engine_cc)


#Q.6?
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Intern(Employee):
#     def calculate_salary(self):
#            print("Intern salary")

# class FullTimeEmployee(Employee):
#      def calculate_salary(self):
#             print("Full Time Employee Salary")

# class ContractEmployee(Employee):
#      def calculate_salary(self):
#             print("Contract Employee Salary")

# intern = Intern()
# fulltimeemployee = FullTimeEmployee()
# contractemployee = ContractEmployee()

# intern.calculate_salary()
# fulltimeemployee.calculate_salary()
# contractemployee.calculate_salary()

#Q. 7?
# Concept: Constructor Overloading (with Default Parameters)
# class Person:
#     def __init__(self, name, age=None, address=None):
#         self.name = name
#         self.age = age
#         self.address = address

# p1 = Person("Vinay")
# p2 = Person("Vinay")
# p3 = Person("Vinay", 22, "Chaksu")

# print(p1.name, p1.age)
# print(p2.name, p2.age)
# print(p3.name, p3.age, p3.address)
        
# Q. 8?
# Concept: Instance & Class Attributes
# class Player:
#      player_count = 0

#      def __init__(self, name, level):
#           self.name = name
#           self.level = level
#           Player.player_count +=1

# p1 = Player("Virat", 10)
# p2 = Player("Rohit", 9)
# p3 = Player("Yashasvi", 8)

# print(p1.name, p1.level)
# print(p2.name, p2.level)
# print(p3.name, p3.level)

# print("Total Players:", Player.player_count)

# Q. 9?
# Concept: Multiple Inheritance
# class Herbivore:
#     def eat_plants(self):
#         print("Eat Plants")

# class Carnivore:
#     def eat_meat(self):
#         print("Eat Meat")

# class Omnivore:
#     def eat_egg(self):
#         print("Eat Egg")

# class Bear(Herbivore, Carnivore, Omnivore):
#     pass

# b1 = Bear()
# b1.eat_plants()
# b1.eat_meat()
# b1.eat_egg()