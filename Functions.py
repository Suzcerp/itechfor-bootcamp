'''
def calc():
    x = 5+4
    return x

y = calc()

print(y+7)
'''

'''
#Positional argument
def calc(b, c):
    a = b + c
    return a
print(calc(3, 4))
'''

#Positional Argument
'''
def intro(name, age, department):
    print(f'Your name is {name}, you are {age} years old and you are in ECE {department}')

intro('Presh', '24', 'ECE')
'''
#Keyword Argument
'''
def intro(name, age, department):
    print(f'Your name is {name}, you are {age} years old and you are in ECE {department}')

intro(age = 24, name = 'Presh', department= 'ECE')


#Default Argument
def intro(name='Presh', age = 24, department = 'MME'):
    print(f'Your name is {name}, you are {age} years old and you are in {department}')

intro(name = 'Michael', age= 24, department='ECE')
'''

import math
def almighty_formula(a,b,c):
    top = abs(b ** 2 - (4 * a * c))
    d = (-b + math.sqrt(top)) / 2 * a
    e = (-b - math.sqrt(top)) / 2 * a
    x = (d, e)
    return x
print(almighty_formula(1,2,3))


def


