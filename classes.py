'''class NameOfClass:
    def name_of_method(self):
        things to do
'''

'''class Character():
    lives(5)
    def __init__(self, name):
        self.name = name
    
    def punch(self, name):
        names.lives -=1
        
#using inheritance
class Boss(Character):
    lives = 10'''

#Bank app
class ItechBank():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        self.balance -=10
        print(f'Your balance is N{self.balance}')

    def deposit(self, amount, depositor):
        self.balance+= amount
        print(f'{depositor} paid in {amount} to your acoount. Your new balance is {self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Your account has been deducted by {amount}. Your new balance is {self.balance}')
            return True
        else:
            print('Insufficient Funds')
            return False

    def transfer(self, amount, user):
        if self.withdraw(amount):
            user.deposit(amount, self.name)


user1 = ItechBank('Ikem Nodebe', 3000)
user2 = ItechBank('Presh', 5000)

#user1.check_balance()
#user2.deposit(5000, 'Lisa')
#user2.withdraw(5000)
user1.transfer(2000, user2)