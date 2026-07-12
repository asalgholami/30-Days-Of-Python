empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0

# list of fruits
b=['12','34','23','100']
n=['ali','sara','asal','matin']
a=['dog','cat','zebra',]
c=['iran','turky','norway']
# Print the lists and it length
print('B:',b)
print('number:',len(b))
print('N:',n)
print('number:',len(n))
print('A:',a)
print('number:',len(a))
print('C:',c)
print('number:',len(c))

# Modifying list

c=['red','Blue','Green','Pink']
s_c=c[2]
print(s_c)
f_c=c[0]
print(f_c)
t_c=c[3]
print(t_c)

# Accessing itmes
n=['sara','matin','asal','sadra']
a=n[-4]
b=n[-2]
print(a)
print(b)

# Slicing items

a=['sara','ali','mehran','matin']
n=a[1:3]
b=a[0:]
s=a[:1]
print(n)
print(b)
print(s)


a=['sara','ali','mehran','matin']
n=a[-1:]
b=a[-3:-1]
s=a[-4:]
print(n)
print(b)
print(s)


a=['sara','ali','mehran','matin']
a[3]='asal'
print(a)
a[0]='mahan'
print(a)
last_index=len(a)
a[last_index-1]='nazanin'
print(a)
# checking items
j=['doctor','ostad','nazanin','student']
does_exist='nazanin' in j
print(does_exist)

# Append
c= ['blue', 'pink', 'green', 'black']
c.append('brown')
print(c)
c.append('red')
print(c)

# insert
n=['ali','sara','iman','nazanin']
n.insert(3,'asal')
print(n)

# remove
f=['12','34','87','100']
f.remove('34')
print(f)
# pop
a=['130','340','900','30']
a.pop()
print(a)
a.pop(1)
print(a)
# del
f = ['banana', 'orange', 'mango', 'lemon']
del f[2]
print(f)
del f[1:3]
print(f)
# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
p_n=['23','4','1','10','23']
m=[20]
n_n=['-1','-12','-9']
integer = p_n + m + n_n
print(integer)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

n_n=['-3','-12','-2']
p_n=['4','23','100']
n=[120]
n_n.extend(n)
n_n.extend(p_n)
print(n_n)

# count
a=['21','32','45','11']
print(a.count(21))

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))
# Reverse
f = ['banana', 'orange', 'mango', 'lemon']
f.reverse()
print(f)
# sort
f = ['banana', 'orange', 'mango', 'lemon']
f.sort()
print(f)
f.sort(reverse=True)
print(f)
