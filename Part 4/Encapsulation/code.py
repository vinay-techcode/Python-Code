# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name #Public Attribute
#         self.__balance = balance #Private attribute - data mangling

#     def get_balance(self): #getter
#         return self.__balance

#     def set_balance(self, new_balance): #setter
#         self.__balance = new_balance

# acc1 = BankAccount("John", 100_000)

# acc1.set_balance(200_000)
# print(acc1.name, acc1.get_balance())

# PQ. - 1?
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, update_salary):
        # self.__salary = update_salary
        if (update_salary >= 0):
             self.__salary = update_salary
        else:
            print("Invalid salary")


e1 = Employee("vinay", 100_000)
e1.set_salary(-200_000)
print(e1.name, e1.get_salary())


        