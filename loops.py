'''
fruits = ['apple', 'banana', 'pineapple', 'paw=paw', 'watermelon' ]
x = 0
while x < len(fruits):
    print(f'{x+1}. {fruits[x]}')
    x+=1
'''

'''
students = [{'name': 'kaykay', 'dept': 'ECE', 'score': 25}, {'name': 'Presh', 'dept': 'ECE', 'score': 50}, {'name': 'Lisa', 'dept': 'ELE', 'score': 45}, {'name': 'Cheta', 'dept': 'ECE', 'score': 27}]

passed_list = []
failed_list = []
x = 0
'''
'''
print("S/N\t Name\t Department\t score")
while x < len(students):
    if students[x]['score'] > 50:
        passed_list.append(students[x])
    else:
        failed_list.append(students[x])
    x += 1
    print(f"{x+1}.\t {students[x]['name']}\t {students[x]['dept']}\t\t {students[x]['score']}")
'''

fruits = ['apple', 'watermelon', 'apple', 'orange', 'banana']

import random
count = 1
for fruit in fruits:
    print(f'{count}.{fruit}')
    count+=1

for i in range(0,100):
    print(random.randrange(1,51))



