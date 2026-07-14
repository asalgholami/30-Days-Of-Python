# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['cisco','VMware','Github'])
print(it_companies)
it_companies.remove('Twitter')
print(it_companies)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
AB=A.union(B)
print(AB)
C=B.issubset(A)
print(C)
m=A.intersection(B)
print(m)
s=A.isdisjoint(B)
print(s)
x=B.symmetric_difference(A)
print(x)

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set=set(age)
print(age_set)
print(len(age))
print(len(age_set))
sentence=' I am a teacher and I love to inspire and teach people'
words=sentence.split()
unique_words=set(words)
print(unique_words)
print(len(unique_words))

