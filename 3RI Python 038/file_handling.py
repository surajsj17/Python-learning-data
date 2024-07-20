# file and mode
import sys
import io

# Set the encoding to UTF-8 for standard output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#mode  = w,x,r,a


#f = open("test.txt","x")
# f = open("test.txt","w")  
# f.write('hello') # single line add
# f.write('\ngood morning')  # single line add
# f.writelines(['\nfirst line','\nsecond line','\nthird line'])  # add multiple lines from a list
# f.close()


# f = open("text.txt","a") #append mode it will add the data as well create the file
# # f.write('\nThis is a python programming langauge') # single line add
# f.writelines(['\nlist','\ntuple','\nstring','\ndict','\nset',])
# # f.close ()


# read() : read the content of the file and return a string format
#readline(): read the content of the file line by line
#readlines(): read the content of the file and returns
# Open the file in read mode

#wap to count the word is present in file  

with open ("text.txt",'r') as f :
    s = f.read()                # Read the first line from the file
data = s.split()
counter = 0
for word in data:
    if 'tuple' in word:
        counter += 1
print("Number of occurrences of 'tuple' :", counter)



    