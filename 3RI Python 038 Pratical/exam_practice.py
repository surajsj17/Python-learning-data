# # # # Write a Python program to take list int numbers from users and returns a new list
# # # # containing only the prime numbers from the original list.


# # # values = int(input("Enter the range of number :"))
# # # list1 = []

# # # for i in range(values):
# # #     str = input(" Enter the number : ")
# # #     if str.isdigit():
# # #         list1.append(int(str))
# # #     else:
# # #         print ("Invalid number Input ")
# # #         exit(1)
# # # print (list1)

# # # num = list1
# # # for x in num:
# # #     for r in range (2,int(x)):
# # #      if x % r == 0:
# # #         print (" Not prime number : ",x)
# # #         break
# # #     else:
# # #       print (" The prime number : ",x)
      
    
        

# # # def decrement(num):
# # #     return (num - 3)
# # # num = int(input("Enter the number : "))
# # # print (decrement(num))

# # # def greter(num,num2):
# # #     if num > num2:
# # #         print ("First Number is greater than second ", num)
# # #     elif num < num2:
# # #         print ("Second Number is greater than first ", num2)
# # #     else:
# # #         print ("First Number and second Number is same ", num, "=", num2)
# # #     return num , num2

# # # greter(12,34)



# # # Given the participants’ score sheet for your University Sports Day, you are required to find
# # # the runner up score. You are given n scores. Store them in a list and find the score of the
# # # runner up.
# # # Explaination: Given list is [2, 3, 6, 6, 5]. The maximum score
# # # is 6, second maximum score is 5.
# # # Hence, we print 5 as the runner up score.


# # list = []
# # try:
# #     num = int(input("Enter the range : "))
# #     for i in range(num):
# #         str = input("Enter the score : ")
# #         if str.isdigit():
# #            list.append(int(str))
# #         else:
# #             raise ValueError("The string is not a valid")
# #     print(f"The score are : {list}")
# #     if len(list) < 2:
# #         raise ValueError("Not enough scores to determine the second minimum score.")
# #     list.sort()
# #     print (f"The maximum score : {list[-1]}")
# #     print (f"The second minimum score : {list[-2]}")
# # except ValueError as e:
# #     print (e)
# # finally:
# #     print ("This is final score")

# num = int(input("Enter the number : "))
# list = []
# try:
#     for i in range(num):
#         str = input("Enter the number : ")
#         if str.isdigit():
#             list.append(int(str)) 
#         else:
#             raise ValueError("Invalid number")
#             exit ()
#     print(list)
# except ValueError as e:
#   print (e)    


# l = [1,2,3,4,5,6,7,8,9,10,11]

# result = list(map(lambda x: x*x ,l))
# print (result)

# result1 = list(filter(lambda x: x % 2 == 0 , l))
# print (f"The even number : {result1}")


# from functools import reduce

# list_largest = [10,80,90,23,1000,44]
# result2 = reduce(lambda x,y: x if x > y else y ,list_largest)
# print (f"The largest number : {result2}")


# class Details:
#     def __init__(self,name,age,id):
#         self.name = name
#         self.age = age
#         self.id = id
#     def display(self):
#         print (f"The name is : {self.name}")
#         print (f"The age is : {self.age}")
#         print (f"The id is : {self.id}")
#     # def __del__(self):
#     #     print ("The object is destroyed")

# d1 = Details("suraj",26,101)
# d1.display()
# print ("*" * 20)
# d1 = Details("sky",22,102)
# d1.display()
# # del d1


list = [1,2,3,4,5,6,7]
print (list[-1::-2]) 
print (list[::])
print (list[3:2:-1])
print (list[:-5:1])
print (list[:-4:-1])
print(list[:-8:-1])
print (list[-1::-1])