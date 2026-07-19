#level 1
#1
age=int(input('Enter your age:'))
if age>=18:
   print('You are old enough to learn to drive.')
else:
   years=18-age
   print(f'you need to wait {years} more years to drive.')
#2
my_age=21
your_age=int(input('Enter your age:'))
if my_age>your_age:
   difference=my_age-your_age
   if difference==1:
       print('I am 1 year older than you.')
    else:
       print(f'I am {difference} years older than you.')
elif my_age<your_age:
   difference=your_age-my_age
   if difference==1:
       print('I am 1 year older than you.')
    else:
       print(f'I am {difference} years younger than you.')
else:
   print('we are the age.')

#3
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
if a>b:
   print('a is greater than b')
elif a<b:
   print('a is smaller than b')
else:
   print('a is equal to b')
#level 2
#1
score=int(input('Enter score: '))
if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('F')
 #2
month=int(input('Enter month: '))
if month=='September' or month=='October' or month=='November':
    print('Autumn')
elif month=='December' or month=='January' or month=='February':
    print('Winter')
elif month=='March' or month=='April' or month=='May':
    print('Spring')
elif month=='August' or month=='June' or month=='July':
    print('Summer')
else:
    print('invalid month')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input('Enter a fruits: ')
if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)
