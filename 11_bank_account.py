# 11_bank_account.py

"""vytvořte soubor 11_bank_account.py

v něm třídu BankAccount, který reprezentuje bankovní účet
třída bude mít attributy
- číslo účtu (str nebo int)
- majitel (stačí jako str)
- stav (konto)

metody
- vložit peníze
- odebrat peníze
- tisknout stav konta

názvy atributů a method vhodně vymyslete"""

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