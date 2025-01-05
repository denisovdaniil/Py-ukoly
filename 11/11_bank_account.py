# 11_bank_account.py

class BankAccount:
    def __init__(self, number, owner, state):
        self.number = number
        self.owner = owner
        self.state = state

    def put_money(self, deposit):
        self.state += deposit
        print(f"The new account state is {self.state}")
    
    def take_money(self, withdrawal):
        self.state -= withdrawal
        print(f"The new account state is {self.state}")

rb = BankAccount(12345, 'Karel', 0)

rb.put_money(1000)
rb.take_money(100)
