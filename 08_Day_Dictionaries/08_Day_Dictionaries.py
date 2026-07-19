dog={}
dog['name'] = 'asal'
dog['color']='pink'
dog['breed']='white'
dog['age']='21'
print(dog)

student= {
    'first_name':'asal',
    'last_name':'gholami',
    'age':21,
    'gender':'female',
    'marital_status':'single',
    'skills':['python','java'],
    'country':'USA',
    'city':'tehran',
    'address':'tehran'
}
#طول دیکشنری
print(len(student))
#بررسی نوع داده skills
print(type(student['skills']))
#اضافه کردن یک یا چند مهارت
student['skills'].append('HTML')
student['skills'].append('C++')
print(student['skills'])
#گرفتن کلید های دیکشنری
print(student.keys())
#گرفتن مقادیر دیکشنری
print(student.values())
#دریافت دیکشنری به لیستی از تاپل ها
print(student.items())
#حذف یک ایتم از دیکشنری
student.pop('age')
print(student)
#حذف کل دیکشنری
del student

