
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

t = (2, 3, 4, 5)
multiple = t[2]
for num in t:
    if(num * multiple):
       
     num = multiple
     num += 1

print(multiple)     

