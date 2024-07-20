# lambda function : anonymous function
# In lambda function we can use numbers of arguments but only expressions



additional = lambda a,b : a + b
print(additional(10,20))

additional1 = lambda a,b : print(a+b)
additional1(10,50)

#filter (function,iterable)
#map (function,iterable)
#reduce (function,iterable)

number = [1,2,3,4,5,6,7]
sum = list(map(lambda x : x ** 2 ,number))
print("Squre : ",sum)

number = [1,2,3,4,5,6,7]
counter = 0
sum = list(filter(lambda x : x % 2 == 0 , number))
print("Even number : ",sum)