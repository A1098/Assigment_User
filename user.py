
class User:
    bank_name = "First National Dojo"
    def __init__(self, name):
        self.name = name
        self.account_balance = 150
    def make_deposit(self, amount):
        self.account_balance += amount
        print(self.name, ", a Deposit of", str(amount), "was successfully processed!")
        print(self.name, ", your account balance is:", self.account_balance)
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        if self.account_balance <= 0:
            print(self.name, "Your account balance is:", self.account_balance)
        else:
            print(self.name, "a withdrawal of", str(amount), "was successfully processed!")
            print("Your account balance is:", self.account_balance)
    def display_user_balance(self):
        print(self.account_balance)
    def transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(self.name, "a transfer of", amount, "was processed to:", other_user.name)
        print(other_user.name, "account balance is now:", other_user.account_balance)
        print("Your account balance is now:", self.account_balance)


Madrid = User("Fidel Madrid")
Ferrencini = User("Francesca Ferrencini")
Ion = User("John Ion")
Madrid.make_deposit(100)
Madrid.make_deposit(50)
Madrid.make_deposit(60)
Madrid.make_withdrawal(200)
Ferrencini.make_deposit(30)
Ferrencini.make_withdrawal(50)
Ferrencini.make_deposit(20)
Ferrencini.make_withdrawal(200)
Ion.make_deposit(1000)
Ion.make_withdrawal(40)
Ion.make_withdrawal(60)
Ion.make_withdrawal(200)
Madrid.transfer(Ion, 50)



