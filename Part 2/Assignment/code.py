# salary = int(input("Enter your salary"))

# if salary <= 30000:
#     print("Tax rate is 5%")
# elif salary <= 50000:
#     print("Tax rate is 15%")
# elif salary <= 70000:
#     print("Tax rate is 25%")

# Write a program to print all numbers from 1 to 100 that are divisible by both 3
# and 5.
# i = 1

# while(i <= 100):
#     if(i%3 == 0 or i%5 == 0):
#      print(i)
#     i += 1

# using for loop
# for i in range(1,101):
#     if(i%3 == 0 or i%5 == 0):
#      print(i)

# Q. 7-> Design a program to continuously input a number n from user & print if it is
# positive or negative until the user enters “Quit”.
# while True:
#     n = input("Enter the number:")

#     if n == "Quit":
#         print("Program Ended")
#         break

#     n = int(n)

#     if(n >0):
#         print("Positive")
#     elif(n < 0):
#         print("Negative")
#     else:
#         print("Zero")


# def even_numbers(a, b):
      
#     for i in range(a, b+1):
#         if(i%2 == 0):
#             print(i)

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# even_numbers(num1,num2) 

# def count_digits(n):
#     count = 0

#     while n > 0:
#        n =  n // 10
#        count += 1

#     return count

# numbers = int(input("Enter the numbers"))
# print(count_digits(numbers))

# def add_digits(n):
#      total = 0

#      while n > 0:
#        digit = n % 10
#        total = total + digit
#        n = n //10

#      return total

# print(add_digits(1234))

# def print_digits(n):
#     reverse = 0

#     while(n >0):
#         digit = n%10
#         reverse = reverse * 10 + digit
#         n = n // 10

#     while reverse > 0:
#         digit = reverse % 10
#         print(digit)
#         reverse = reverse // 10

# print_digits(312)  

# def calculator(a,b, operation):
#     if (operation  == "+"):
#      return a + b
#     elif(operation == "-"):
#        return a - b
#     elif(operation == "*"):
#        return a * b
#     elif(operation == "/"):
#        return a / b
#     else:
#        return "invailid operation"

# print(calculator(4,5,"+"))

# def is_Prime(n):

#     if (n < 2):
#         return False

#     for i in range (2, n):
#         if(n%i == 0):
#             return False
#     else:
#       return True

# print(is_Prime(6))

# secret_number = 25
# guess = int(input("Guess the number: "))

# if(guess > secret_number):
#     print("To High")
# elif(guess < secret_number):
#     print("To Low")
# elif(guess == secret_number):
#     print("Correct!")
  