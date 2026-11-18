# string = "hello"

# if 'x' in string:
#   print("o exists in string")
# else: 
#   print("not exist")
#in => membership oerator

# for var in string:
#  print(var)


# for i in range(5):
#  print( "hello")

# word = "artificial intelligence"

# #count the number of i's => 5

# count = 0
# for ch in word:
#     if(ch == 'i'):
#         count += 1

# print("count of i =", count)


# vowel count
# word = "artificial"
# count = 0

# for ch in word:
#     if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count += 1
     
# print("ans = ",count)
# for i in range(0,10,3):
#     print(i)

#print sum of 'n' natural numbers
# n = int(input("Enter number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i

# print(sum)

#print 1 to 10
# for i in range (1, 11):
#     print(i)

# n = int(input("enter number"))
# for i in range (1, 11):
#    print(n*i)

#add 1 to 100 numbers
# n = int(input("enter number"))
# sum = 0
# for i in range(2, n +1,  2):
#  sum += i
 
#  print(sum)


# n = int(input("enter number"))
# for i in range(1, n + 1):
#     print(i*i)

#factorial of a number
# fact = 1
# for i in range(1, 6):
#     fact = fact * i
   
# print(fact)

# fruits = ["Apple", "Banana", "Mango", "Orange"]
# for i in fruits:
    
#  print(i)

# numbers = [10, 20, 30, 40, 50]
# for i in numbers:
#     print(i)

# n = int(input("enter number: "))
# for i in range(1, n + 1):
#     if(n % i == 0):

#      print(i)

# n = int(input("enter number: "))
# count = 0
# for i in range(1, n+1):
#    if(n % i == 0):
#         count += 1

# if count == 2:
#     print("prime number")
# else:
#     print("not prime number")

n = 15 
count = 0
for i in range(1, n + 1):
    if(n % i == 0):
        count += 1


if(count == 2):
        
        print("prime")

else:
       
     print("not prime")
