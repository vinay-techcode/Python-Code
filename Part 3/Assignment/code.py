# PQ -> Eg
# word = "madam"
# reverse = word[::-1]
# print(reverse)

# name = "vinay"
# print(name[::-1])

# numbers = [10, 20, 30, 40, 50]
# print(numbers[::-2])

# word = input("Enter the word: ")
# reverse = word[::-1]
# if(word == reverse):
#     print("Pelindrome")
# else:
#     print("Not Pelindrome")    

numbers = [10, 20, 30, 40, 50, 60]
total = 0
for num in numbers:
    total = total + num
average = total/len(numbers)

print(average)