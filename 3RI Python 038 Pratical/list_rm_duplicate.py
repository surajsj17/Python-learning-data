list = [1,2,3,2,5,1,7,3,9,2,5,9]
newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print ("Removed the duplicate value : ", newlist)
for listed in newlist:
    print (listed)