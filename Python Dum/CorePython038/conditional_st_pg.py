# conditional statements
# if ..else..elif
# if st.. syntax:
# if  condition(relational,compa,logical):
# statements (print)

# wap to take  2 int numbers from user and find largest number.
# n1 = int(input("Enter num1:"))  # 20   #  30
# n2 = int(input("Enter num2:"))  # 5    # 50

# if n1 > n2:  # true /false  # 20 > 5 -->  True   # 30 >50 --> false
#     print(n1, "is largest")  # 20 is largest
#     print("done")
# else:
#     print(n2, "is largest")
# print("code is done bye....")

# wap to check entered password and confirm password are same or not..
# pwd = input("enter password:")  # asd
# cf_pwd = input("enter confirm pwd:")  # asd

# if pwd == cf_pwd:  # --> False (msg -->else)  # asd1 == asd123 --> false
#     print("valid")  # valid
# else:
#     print("invalid")

# find largest int number between 3 int numbers.
# elif --> stat..
# 20 ,30,50
# a, b, c = 30, 20, 50
# if a > b and a > c:  # --> false  a is not largest
#     print(a, "is largest")
# elif b > c and b > a:  # --> fale  b is not largest
#     print(b, "is largest")
# else:
#     print(c, "is largest")

"""
if condition:
elif 
elif
elif
else
"""
# or :
# wap to check entered character is vowel or not : a,e,i,o,u
# ==
ch = input("Enter character:")  # d   #u
if ch == "a":  # d == 'a' --> f   u == 'a' --> f
    print("yes", ch, "is vowel")
elif ch == "o":  # d == 'a' --> f  'u' == 'o' --> f
    print("yes", ch, "is vowel")
elif ch == "i":
    print("yes", ch, "is vowel")
elif ch == "e":
    print("yes", ch, "is vowel")
elif ch == "u":  # 'u' == 'u' --> t
    print("yes", ch, "is vowel")
else:
    print("its not vowel")
print("$"*100)

if ch == "a" or ch == "e" or ch == "i" or ch == "u" or ch == "o":  # true
    print(ch, "is vowel")
else:
    print(ch, "not vowel")
print("$"*100)


