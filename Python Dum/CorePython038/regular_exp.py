import re
# regular expression : 'it's is a sequence of characters that
# forms a search pattern'
# findall() - returns a list containing all matches
# finditer() - returns an iterator containing all matches
# search() - returns a match object if there is a match
# split() - returns a list where the string has been split at each match
# sub() - replaces one or many matches with a string
# match() - returns a match object if there is a match at the beginning of the string
# finditer() - returns an iterator containing all matches

# findall() - returns a list containing all matches
s = "we learn python python is easy python is powerful language"
print(re.findall('python',s)) # ['python', 'python', 'python']

username = 'suvidha'
print(re.findall('a',username)) 

# finditer() - returns an iterator containing all matches
it = re.finditer('python',s)
print(it)
for i in it:
    print(i)

# search() - returns a match object if there is a match
username = 'suvidha'
pattern = '[aeiou]'  # any one vowel in username

if re.search(pattern,username):
    print('user is valid ')
else:
    print('user is invalid')

# match() - returns a match object if there is a match at the beginning of the string
# username first_letter should be in uppercase
username = 'Suvidha'
pattern = '[A-Z]' # '[0-9A-Z]' # '[aeiou]'

if re.match(pattern,username):
    print('user is valid ')
else:
    print('user is invalid')
    

# sub() - replaces one or many matches with a string
s = "we learn python python is easy python is powerful language"
print(re.sub('python','java',s)) # we learn java java is easy java is powerful language

# write a python program to validate email id using regular expression

email = input("Enter an email address: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

