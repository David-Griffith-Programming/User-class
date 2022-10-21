class User:
    # ! CONSTRUCTOR FUNCTION!!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = 0

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"{self.first_name} {self.last_name}, Balance:${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount 

heav = User("Heav", "Griffith", 20)
david = User("David", "Griffith", 23)
steve = User("Steve", "Griffith", 65)



heav.make_deposit(100)
heav.make_deposit(100)
heav.make_deposit(100)
heav.make_withdrawal(100)
heav.display_user_balance()
david.make_deposit(200)
david.make_deposit(200)
david.make_withdrawal(100)
david.make_withdrawal(10000)
david.display_user_balance()
steve.make_deposit(100000)
steve.make_withdrawal(100000000000000)
steve.make_withdrawal(10000000000000000000000)
steve.make_withdrawal(10000000000000000000000)
steve.display_user_balance()
heav.transfer_money(steve, 10000)
print(heav.account_balance)
print(steve.account_balance)
















































