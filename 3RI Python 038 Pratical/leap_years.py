#leap years from    

year = int(input("Enter the year to check leap year : "))  # year to check  
if (year % 400 == 0) or  (year % 4 == 0 and year % 100 != 0 ) :
    print(year, "is a leap year")
else :
    print(year, "is not a leap year") 
    
