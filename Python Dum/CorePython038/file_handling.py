# open('file_name','mode'): opens a file in the specified mode and returns a file object
# with open() as file_object:
# test1.txt
# mode : x: create
# w: write
# r: read
# a : append
# f = open('test1.txt', 'x')
# f = open('test1.txt', 'w')
# # write() : writes the content to the file
# f.write('Hello World')
# f.write("\nwe learn python")
# # writelines() : writes a list of lines to the file
# f.writelines(['\nGm all \n','we learn python Programming\n','Python is easy to learn\n'])
# f.close()

# a: append
# f = open('test1.txt', 'a')
# f.write('\nwe learn file handling concept')
# f.writelines(['\nfile handling has diff mode\n','append,write,read,create modes are included in file handling'])
# f.close()
# r: read
f = open('test1.txt', 'r')
# read() : reads the content of the file and returns
# a string format
# readline() : reads the content of the file line by line
# readlines() : reads the content of the file and returns 
#a list of lines
# s = f.read()
# print(s,type(s))

# if 'JAVA' in s:
#     print('Yes')
# else:
#     print('No')

# x = f.readline()  # 1
# print(x)
# print(f.readline()) # 2
# f.readline() #3
# print(f.readline()) # 4

l = f.readlines()
print(l)

# wap to find the total no of lines present in test1.txt.
print(len(l))

# wap to find the total no of words present in test1.txt.
s = f.read()
words = s.split()
print(len(words))