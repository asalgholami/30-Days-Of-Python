#level 1
empty_tuple=()
name_s=('nazanin','baran','asal')
print('sisters:',name_s)
name_b=('ali','mehran','mahdi')
print('brothers:',name_b)
siblings=name_s+name_b
print('siblings:',name_s+name_b)
print('number of siblings:',len(siblings))
family_members=list(siblings)
family_members.extend(['mostafa','donya'])
print(family_members)

#level 2
*siblings,father,mother=family_members
parents=(father,mother)
print(parents)
print(siblings)
#creat tuples
fruits_tp=('apple','banana','orange')
vegetables_tp=('carrot','potato','tomato')
animal_products_tp=('milk','egg','cheese')
food_stuff_tp=fruits_tp+vegetables_tp+animal_products_tp
print(food_stuff_tp)
food_stuff_li=list(food_stuff_tp)
print(food_stuff_li)
middle=food_stuff_li[3:6]
print(middle)
print(food_stuff_li[:3])
print(food_stuff_li[3:6])
del food_stuff_tp
print('egg' in food_stuff_li)