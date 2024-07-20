# write the program to check the days by input the number by the user

days = int(input("Enter a Day Number :"))

if days == 1:
    print ("..Monday..")
elif days == 2:
    print ("..Tuesday..")
elif days == 3:
    print ("..Wednesday..")
elif days == 4:
    print ("..Thursday..")
elif days == 5:
    print ("..Friday..")
elif days == 6:
    print ("..Saturday..")
elif days == 7:
    print ("..Sunday..")
else:
    print ("..Invalid days ..")
    exit()


'''
OUTPUT - Enter a Day Number :4
         ..Thursday..
'''
