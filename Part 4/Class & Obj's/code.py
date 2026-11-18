# class Student:
#     subject = "Python"
#     college = "ABC"
#     year = "4th year"

# stu1 = Student()
# stu2 = Student()
# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)


# class Student:
#     subject = "Python"
#     college = "ABC"
#     year = "4th year"

# stu1 = Student()
# print(type(stu1))



#Constructor Method
# __init__ Method
# class Student:

#     def __init__(self):
#         print("obj is being constructor")

#     def __init__(self, name, age): #Parameterized Constructor
#         self.name = name
#         self.age = age

#     def get_age(self):
#         return self.age
    
# stu1 = Student("Vinay", 22)
# stu2 = Student("Urvashi", 23)
# stu3 = Student("Shradha", 21)

# print(f"{stu1.name} of age = {stu1.get_age()}")


# class Student:
#     name = "vinay"
#     age = 22

# s1 = Student()
# print(s1.name)

# class Car:
#     brand = "Toyota"
#     color = "Black"

# c1 = Car()
# c2 = Car()
# c2.brand = "BMW"
# c2.color = "Blue"
# print(c1.brand, c1.color)
# print(c2.brand, c2.color)

# class Student:
#     name = "vinay"

# s1 = Student()    
# s2 = Student()

# s1.name = "Rahul"
# s2.name = "Aman"

# print(s1.name)
# print(s2.name)

# class Mobile:
#     brand = "Samsung"
#     price = 15000

# m1 = Mobile()    
# m2 = Mobile()

# m1.brand = "Apple"
# m2.brand = "Vivo"

# print(m1.brand)
# print(m2.brand)

# class Employee:
#     name = "Unknown"
#     salary = 10000

# e1 = Employee()   
# e2 = Employee()

# e1.name = "Rahul"
# e1.salary = 20000

# e2.name = "Amit"
# e2.salary = 25000

# print(e1.name, e1.salary)
# print(e2.name, e2.salary)

# class Student:
#     def __init__(self):
#         self.name = "Vinay"
#         self.age = 22

# s1 = Student()

# print(s1.name, s1.age)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Vinay", 22)
# s2 = Student("Saniya", 21)
# print(f"{s1.name} of age {s1.age}")
# print(f"{s2.name} of age {s2.age}")


# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# c1 = Car("G-Wagon", "Black")
# c2 = Car("Lamborghini", "Blue")
# print(f"{c1.color} color of {c1.brand}")
# print(f"{c2.color} color of {c2.brand}")


# class Mobile:
#     def __init__(self, brand, price, ram):
#        self.brand = brand
#        self.price = price
#        self.ram = ram

# m1 = Mobile("Apple", 100000, "1TB")
# m2 = Mobile("Samsung", 75000, "8GB")

# print(m1.brand, m1.price, m1.ram)
# print(m2.brand, m2.price, m2.ram)

# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def get_salary(self):
#         return self.salary

# e1 = Employee("Vinay", "15LPA", "IT")
# e2 = Employee("Anil", "12LPA", "Civil")

# print(e1.name, e1.salary, e1.department)
# print(e2.name, e2.salary, e2.department)

# print(f"{e1.name} of  salary = {e1.get_salary()}")

# class Student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     def get_marks(self):
#         return self.marks

# s1 = Student("vinay", 99)
# s2 = Student("shiva", 80)

# print(s2.name, s2.marks)
# print(f"{s1.name} marks of {s1.get_marks()}")

