# Function Overriding
# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher (Employee):
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

# Duck Typing
class Teacher():
    def get_designation(self):
        print("designation = Employee")

class Acountent():
    def get_designation(self):
        print("designation = Acountent")

t1 = Teacher()
t1.get_designation()

acc1 = Acountent()
acc1.get_designation()