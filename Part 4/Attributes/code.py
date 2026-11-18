# class Student:
#     college_name = "ABC college"  #class attribute
#     PI = 3.1 

#     def __init__(self, name, gpa):     #instance attribute
#        self.name = name
#        self.gpa = gpa
#        self.PI = 3.14

# stu1 = Student("Vinay", 9.2)

# print(Student.name)

#Instance Method
# class Laptop:
#     storage_type = "ssd"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storage = storage

#     @classmethod
#     def get_storage_type(cls):
#         print(f"storage type = {cls.storage_type}")   

#     def get_info(self): #Instance Method
#         print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

#     @staticmethod
#     def calc_discount(price, discount):
#         final_price = price - (discount * price/100)
#         print(f"Discount price = {final_price}")
# l1 = Laptop("16gb", "512gb")


# l1.calc_discount(40_000, 10)

# class Product:
#     count = 0

#     def __init__(self, name,price):
#         self.name = name
#         self.price = price
#         Product.count += 1

#     def get_info(self): #Instance Method
#         print(f"Price of {self.name} is Rs. {self.price}")

#     @classmethod
#     def get_count(cls):
#         print(f"Total products in store = {cls.count}")

#     @staticmethod
#     def calc_discount(price, discount):
#         print(f"discounted price = {price - (price * discount/100)}")

# p1 = Product("phone", 10_000)
# p2 = Product("laptop", 50_000)
# p3 = Product("pen", 10)

# p1.calc_discount(p1.price, 50)

# class Employee:
#     company_name = "Google"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self): #Instance Method
#         print(f"{self.name} salary is {self.salary} in {self.company_name} ")

#     @classmethod
#     def change_company(cls, new_company):
#         cls.company_name = new_company
        

#     @staticmethod
#     def valid_salary(salary):
#         print(f"valid salary is {salary < "13LPA"}")
        
# e1 = Employee("Vinay", "15LPA")    
# e2 = Employee("Anil", "17LPA")


# Employee.change_company("Microsoft")
# e2.show_details()

# Employee.valid_salary("10LPA")

# class Student:
#     school_name = "ABC School"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def show_details(self): #Instance Method
#         print(f"{self.name} marks is {self.marks} from {self.school_name}")

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school_name = new_school

#     @staticmethod
#     def cheak_result(marks):
#       if(marks >= 33):
#             print("pass")
#       else:
#          print("Fail")      

# s1 = Student("Ramu", 30)
# s2 = Student("Shyamu", 80)


# Student.change_school("XYZ")
# s1.show_details()

# s1.cheak_result(s1.marks)

# class BankAccount:
#   bank_name = "SBI"

#   def __init__(self, name, balance):
#     self.name = name
#     self.balance = balance

#   def show_balance(self):
#     print(f"{self.name} balance is {self.balance} in {self.bank_name}")

#   @classmethod
#   def change_bank(cls, new_bank):
#    cls.bank_name = new_bank 

#   @staticmethod
#   def cheak_balance(balance):
#         if(balance > 500000):
#            print("Sufficient Balance")

#         else:
#            print("Low Balance")

# b1 = BankAccount("vinay", 1_0000_000)
# b2 = BankAccount("Anuj", 1_000000)


# BankAccount.change_bank("BOB")
# b1.show_balance()
# b2.show_balance()
# b1.cheak_balance(b1.balance)