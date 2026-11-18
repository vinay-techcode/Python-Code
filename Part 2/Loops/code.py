# count = 100
# while (count >= 0):
#     print(count)
#     count -=1

# multiplication table of any number
# n = int(input("enter num: "))


#Factorial of a number
# n = int(input("enter number"))
# i = 1;
# fact = 1
# while (i <= n):
#     fact = fact * i
#     i = i + 1
#     print(fact)

# n = int(input("Enter Number"))
# count = 0

# if (n == 0):
#      count = 1
# else: 
#    while n > 0:
#         count = count + 1
#         n = n // 10

# print(count)  

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0 #initialization
# while idx < len(nums):
#         print(nums[idx])
#         idx += 1

# i = 1

# while (i >= 1):
#     print(i)
#     i -= 1

# n = int(input("Enter num: "))

# i = 1
# while(i <= 10):
#     print(n * i)
#     i += 1

#. Factorial of a number

# n = int(input("Enter Number"))
# i = 1
# fact = 1

# while i <= n:
#     fact = fact * i
#     i +=1 

# print(fact)

# 1 se 10 tak numbers print
# i = 10
# while(i >= 1):

#     print(i)
#     i -= 1 

# n = int(input("Enter num: "))
# i = 1
# while(i <= 10):
#     print(i * n)
#     i += 1

# n = int(input("Enter number: "))
# i = 1
# fact = 1
# while(i <= n):
#     fact = fact * i
#     i += 1
# print(fact)

# n = int(input("enter num: "))
# i = 1
# while(i <= n):
#     print(i)
#     i += 1
# n = int(input("enter the num: "))
# i = 1
# sum = 0
# while(i <= n):
#     sum = sum + i
#     i += 1
    
# print(sum)

# n = int(input("enter number"))
# total = 0

# while n > 0:
#     digit = n % 10
#     total = total + digit
#     n = n // 10
# print(total)


# n = int(input("enter the number: "))
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(rev)


# break & continue
# n = int(input("enter number"))
# i = 1
# while(i <= 10):
#     print(n * i)
#     i += 1

# i = 1
# while(i <= 10):
#     if(i % 6 == 0):
#      break

#     print(i)
#     i += 1

# print("outside the loop") 

# i = 0
# while(i < 10):
#     i += 1
#     if(i % 2 == 0):
#         continue
#     print(i)
    
# print("outside loop now...")

#print quebe 1 to 5
# n = int(input("enter number"))
# num = 1
# while(num <= n):
#     print(num ** 4)
#     num += 1

# List Methods 
# 1st.-> I.append
# nums = [1, 2, 3, 4]
# nums.append(5)
# print(nums)

# nums.insert(2,11)
# print(nums)

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

# loops in lists
# nums = [1, 2, 3, 4, 5,]
# for val in nums:
#     print(val)

# pq. ->
# nums  = [1, 2, 3, 4, 11, 13]
# x = 11
# idx = 0

# for val in nums:
#   if(val == x):
#     print(f"{x} fount at  idx = {idx}")
#     break
#   idx += 1