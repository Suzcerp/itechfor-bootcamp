#try except, else and finally
'''
try:
    num = (int(input('How old are you:')))
    print(num + 5)
except ValueError as e:
	print('You can ony pass in numbers, try again!')
except:
	print('You have made a mistake')
else:
    print('You are good to go')
finally:
    print('You have entered the finals!')
'''

def odd_even(a):
        if ((a) % 2) == 0:
            print('it is an even number')
        else:
            print('it is an odd number')
try:
    num = (int(input('Enter a number:')))
    odd_even(num)
except ValueError as e:
    print("You can only pass numbers")





