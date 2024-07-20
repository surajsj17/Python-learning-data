# write the program to entered the year is the leap year or not

years = int(input("Enter the Year : "))

# years % 400 is use for century years and for leap years you can used (years % 4 == 0 and years % 100 != 0 )
if years % 400 == 0 or (years % 4 == 0 and years % 100 != 0 ):
    print ("The year is leap year :",years)
else:
    print("The year is not leap year :",years)

'''
OUTPUT - 
Enter the Year : 2024
The year is leap year : 2024
'''