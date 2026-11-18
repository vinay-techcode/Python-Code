# Q - 1.->
# name = "vinay badoliya"
# print(len(name))

# Q - 2.->
# text = "python"
# print(text[0])
# print(text[4])
# print(text[5])

# Q - 3.->
# text = "programming"

# print(text[0 : 4])
# print(text[0 : ])

# Q - 4.->
# name = "vinay badoliya"
# print(name.upper())
# print(name.lower())

# Q - 5.->
# text = "banana"

# print(text.count("a"))

#Formatting Q's. practice
# Q - 1.->
# name = "vinay"
# age = 22
# print("my name is {} and my age is {}".format(name,age)) #{} = Placeholder (jahan value aayegi).

# Q - 2.->
# a = 10 
# b = 20
# print("The value of a is {} & b is {}".format(a,b))

# Q - 3.->
# name = "vinay"
# course = "AI ML"
# print("{} is learning {}".format(name,course))

# Q - 4.->
# name = "vinay"
# age = 22
# city = "jaipur"
# print("my name is {}, I am {} years old I Live in {}".format(name,age,city))

# Q - 5.->
# name = "vinay"
# course = "Data Science"

# print("I am learning {1} and my name is {0}".format(name,course))

# Q - 6.->
# print("{0} {1} {0}".format("Hello", "Python"))

# name = "vinay"
# age = 22
# salary = 100000
# print("name {}, age {}, salary {}".format(name, age, salary))

# Q - 7.->
# price = 99.5678

# print("Price is {:.2f}".format(price))
# Q - 8.->
# name = "Vinay"
# marks = 87.567

# print("Student: {0}, Marks: {1:.2f}".format(name, marks))

#F-String Method
# Q - 1.->
# name = "Vinay"
# age = 22
# print(f"My name is {name} and my age is {age}")

# Q - 2.->
# a = 10
# b = 20
# print(f"sum is {a + b}")

# Q - 3.->
# price = 99.5678

# print(f"Price is {price:.2f}")

# name = "vinay"
# city = "jaipur"

# print(f"My name is {name} and I Live in {city}")


#Lists Practice Questions
# Q - 1.->
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total = total + num

# print(total)

# Q - 2.->
# numbers = [12, 45, 7, 89, 23]
# largest  = numbers[0]

# for num in numbers:
#     if(num > largest):
#         largest = num

# print(largest) 


# Q - 3.->
# numbers = [10, 15, 20, 25, 30, 35, 40]

# for num in numbers: 
#    if(num % 2 == 0):
#       print(num)

# Q - 4.->
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.reverse()
# print(numbers)

# Q - 5.->
# numbers = [11, 12, 12, 14, 14, 15, 16, 17, 17]
# unique = []
# for num in numbers:
#  if num not in unique: 
#     unique.append(num)
#  else:
#    print(num)

# Q - 5.->
# numbers = [10, 20, 10, 30, 40, 10, 20 , 50, 30]

# unique = []
# duplicates = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

#     elif num not in duplicates:
#       print(num)
#       duplicates.append(num)

#Tuple practice questions
# tup = (10, 20, 30)
# print(tup[0])
# print(tup[2])

# tup = [1, 2, 3, 4, 5, 6, 7, 8]
# print(tup[-1])
# print(tup[-4:-1])
# print(tup[1:3])

# t = (10, 20, 30, 20, 40, 20, 50)
# print(len(t))
# print(t.count(20))
# print(t.index(40))
# print(t[::-1])

# t = (12, 15, 20, 25, 30, 35, 40)
# total = 0

# for num in t:
#     if(num%2 == 0):
#         total = total + num

# print(total)

# t = (45, 12, 89, 23, 67, 10)
# largest = t[0]
# for num in t:
#     if(num > largest):
#         largest = num

# print(largest)

# t = (10, 15, 20, 25, 30, 35, 40)
# newTuple = []
# for num in t:
#     if(num%2 == 0):
#         newTuple.append(num)

# print(tuple(newTuple))

# t = (2, 3, 4, 5)
# total = 1
# for num in t:
#         total = total * num
#         num  += 1

     
# print(total)

t = (10, 20, 10, 30, 20, 40, 50)
unique = []
for num in t:
    if num not in unique:
        unique.append(num)

    else:
        print(num)     



