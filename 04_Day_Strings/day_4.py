
# Single line comment
letter = 'F'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, Asal'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
Se = ("nice to meet you ")
print(Se)

# Multiline String
multiline_string = '''I am a student and i am learning python'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asal'
last_name = 'Gholami'
space = ' '
full_name = first_name + space + last_name
print(full_name)
# Checking length of a string using len() builtin function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Unpacking characters
language = 'nazanin'
a, b, c, d, e, f , g = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f) # n
print(g)

# Accessing characters in strings by index
language = 'Bodylanguage'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[5]
print(second_letter)  # y
last_index = len(language) - 2
last_letter = language[last_index]
print(last_letter)  # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing

language = 'Bodylanguage'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Bodylanguage'
A = language[1:6:2]
print(A)

# Escape sequence
print('How old are you?.\n45?')
print('Time\tDays\tminuts')
print('Time1\t1\t12')
print('Time2\t7\t30')
print('In every programming language it start \"it is difficult!\"')

# String Methods
# capitalize(): Converts the first character the string to Capital Letter

l_n='piece of cake'
print(l_n.capitalize())

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

l_n='piece of cake'
print(l_n.count('e'))
print(l_n.count('c'))

# endswith(): Checks if a string ends with a specified ending

challenge = 'piece  of cake'
print(challenge.endswith('e'))   #True
print(challenge.endswith('ke'))  #True

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
l_n='Girl\tAli\tschool'
print(l_n.expandtabs())
print(l_n.expandtabs(20))

# find(): Returns the index of first occurrence of substring
P1='piece of cake'
print(P1.find('i'))
print(P1.find('a'))
print(P1.find('k'))

# format()	formats string into nicer output
f='Asal'
l='Gholami'
j='student'
s='I am {} {}. I am a {}.' .format(f,l,j)
print(s)

radius=15
pi=3.14
a=pi
R='The area of circle with {} is {}'.format(str(radius),str(a))
print(R)

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha())  # True
num = '110'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters
A='Asal gholami'
print(A.isdecimal())
A='453'
print(A.isdecimal())
A='6 9'
print(A.isdecimal())


# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y'))  # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False
