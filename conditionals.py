age = int(input('how old are you:'))
department= input('what department are you:')
'''
if, else, elif statement
if age < 18:
	print('You are too young to access this')
elif age>=18 and age<=30:
	print('You are a youth!')
elif age>30 and age<=95:
	print('You should marry!')
else:
	print('God pass you')
'''
#Nested if
if age > 18:
	print('You are a youth')
else:
	print('You are too young')

	if department == "ECE":
		print('You are welcome to ECE!')
	else:
		print('We do not recognize this department')
