#Student Enrolments
# ->list all courses
# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]
# print(info)
# for tup in info:
#     # print(tup[0]) #names
#     print(tup[1]) #courses

# #unique courses
# courses_set = set()
# for tup in info:
#     courses_set.add(tup[1])

# print(courses_set)

#print students names only english course
# for name, courses in info:
#     if(courses == "English"):
#       print(name)

#cretae dictionary (student, set of courses)

# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]
# dict = {}

# for name, courses in info:
#     if(dict.get(name) == None):
#        dict.update({name: set()})
#        dict[name].add(courses)

#     else: 
#         dict[name].add(courses)
# print(dict)

# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English")
# ]
# students = set()
# for student, course in info:
#      students.add(student)

# print(students)

# Q. -> 3?
# list1 = [1, 2, 7]
# list2 = [2, 4, 5]
# result = list1 + list2
# result.sort()
# print(result)

# Q. 4 (1)
#  A tuple of all even numbers
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for num in tuple:
#     if(num%2 == 0):
#         print(num)

# Q. 4 (2)
# A tuple of all odd numbers
# tuple = (12, 45, 56, 37, 91, 58, 83, 90, 47, 72)
# for num in tuple:
#     if(num%2 != 0):
#         print(num)

# Q. -> 5?
# studentData = {
#     "vinay": 90,
#     "Anil":  78,
#     "Shiva": 56,
#     "Anuj":  85,
#     "Vipul": 65,
#     "Vinod": 72
# }
# A - Add a student
# studentData["Shayam"] = 43
# print(studentData)

# B – Update marks
# studentData["vinay"] = 99
# print(studentData)

# C – Search for a student

# if "vinay" in studentData:
#     print(studentData["vinay"])

# D- Display all students and marks
# for name, marks in studentData.items():
#     print(name, marks)

# Q. -> 6
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# wordLength = {}
# for word in words:
#    wordLength[word] = len(word)

# print(wordLength)

# Q. -> 7
# sentence = input("Enter the sentence: ")
# count = 0
# for char in sentence:
#     if(char == " "):
#         count += 1

# print("Number of spaces: ", count)

# Q. -> 8?
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6, 7]

# set1 = set(list1)
# set2 = set(list2)

# if set1 & set2:
#     print("Comman Elements Found")

# else:
#     print("No comman Elements")

# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]

# set1 = set(list1)
# set2 = set(list2)

# comman = set1 & set2

# if comman:
#     print("Comman Elements found:", comman)
# else:
#     print("No Comman Elements")


# Q. -> 9?
# numbers = [10, 20, 30, 10, 40, 20, 50, 60, 40]
# seen = set()
# repeated = set()
# for num in numbers:
#     if num in seen:
#         repeated.add(num)
#     else: 
#         seen.add(num)

# print(repeated)     

# Q. -> 10?
text = input("Enter a string")

unique = set(text)
print("Unique Characters: ", unique)
print("Count of Unique Characters: ", len(unique))
