# class Employee:
#     start_time = "10Am"
#     end_time = "5Pm"
 
#     def change_time(self, new_end_time):
#        self.end_time = new_end_time
       
# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# staff1 = AdminStaff("Manager")
# staff1.change_time = "5Pm"
# print(staff1.role, staff1.start_time, staff1.end_time)
        

#Multilevel Inheritance
# class Employee:
#     start_time = "10Am"
#     end_time = "5Pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountent(AdminStaff):
#     def __init__(self, salary, role):
#        super().__init__(role)
#        self.salary = salary

# acc1 = Accountent(100_000, "CA")

# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

#Multiple Inheritance
# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class Student:
#     def __init__(self, gpa):
#         self.gpa = gpa

# class TA(Teacher, Student):
#     def __init__(self, salary, gpa, name):
#         super().__init__(salary)
#         Student.__init__(self, gpa)
#         self.name = name

# ta1 = TA(100_000, 9.9, "vinay")

# print(ta1.name, ta1.salary, ta1.gpa)

# Single level Inheritance PQ. ->
# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def show_vehicle(self):
#         print(f"{self.brand} color of {self.color}")

# class Car(Vehicle):
#     def __init__(self, model, brand, color):
#         self.model = model
#         super().__init__(brand, color)

#     def show_car(self):
#         print(f"{self.brand} {self.color} {self.model}")


# c1 = Car("Totota", "Black", "fortuner")
# c1.show_car()

        
# Multi level Inheritance PQ. ->
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print("Eating Food")

# class Dog(Animal):
#     def __init__(self, breed, name):
#         self.breed = breed
#         super().__init__(name)

#     def bark(self):
#         print("dog is barking")

# class Puppy(Dog):
#     def __init__(self, name, breed, age):
#         self.age = age
#         super().__init__(breed, name)
      

#     def play(self):
#         print("puppy is playing")  

# p1 = Puppy("rocky", "French Bulldog", "5 Year")
# print(p1.name)
# p1.eat()
# print(p1.breed)
# p1.bark()
# print(p1.age)
# p1.play()   

#Multiple Inheritance
# class Teacher:
#     def __init__(self, subject):
#         self.subject = subject


#     def teach(self):
#         print("Teaching Python")

# class Reasearcher:
#     def __init__(self, field):
#         self.field = field

#     def reasearch(self):
#         print("Researching AI")

# class Proffesor(Teacher, Reasearcher):
#     def __init__(self, name, subject, field):
#         self.name = name
#         super().__init__(field)
#         Teacher.__init__(self, subject)   

# p1 = Proffesor("Vinay", "Python", "AI")
# print(p1.name)
# p1.teach()
# p1.reasearch()



 