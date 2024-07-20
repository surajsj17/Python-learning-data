# A candidate is recruited based on following criteria:
# if male,age should be above 30 year and height above 160
# if female,age should be above 25 year and height above 155    


gender = input("Gender : ")
age = int(input("Age : "))
height = float(input("Height : "))

if gender == "male" and age >= 30 and height >= 160:
    print ("The Male candidate is fit in criteria " )
elif gender == "female" and age >= 25 and height >= 155:
    print ("The Female candidate is fit in criteria " )
else:
    print ("The candidate is not fit in criteria !! " )


'''
OUTPUT - 
Gender : male
Age : 22
Height : 123
The candidate is not fit in criteria

'''