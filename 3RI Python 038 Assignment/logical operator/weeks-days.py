# write the program to for print weeks day and weekend day as user enetered the number 1,2,3,4,5,6,7

days = int(input(" Enter the number of days :"))

if days == 1 or days == 2 or days == 3 or days == 4 or days == 5:
    print (" It's week days !!")
elif days == 6 or days == 7:
    print(" It's Weekend !!")
else:
    print(" It's Invalid Number !!")
    
'''
OUTPUT - 
Enter the number of days :1
 It's week days !!
'''
    