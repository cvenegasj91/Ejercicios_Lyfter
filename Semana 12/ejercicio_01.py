class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposito de {amount} realizado a su cuenta' + f'\nNuevo saldo de: {self.balance}')
        else:
            print("Debe depositar una cifra mayor a cero")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Retiro de {amount} realizado a su cuenta' + f'\nNuevo saldo de {self.balance}')
        else:
            print("Saldo insuficiente")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        self.min_balance = min_balance
        super().__init__(balance)

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Error: Saldo por debajo del minimo")
        else:
            super().withdraw(amount)


cuenta1 = BankAccount(100)
cuenta1.deposit(50)
cuenta1.withdraw(25)
cuenta1.withdraw(150)

cuenta2 = SavingsAccount(100, 25)
cuenta2.deposit(50)
cuenta2.withdraw(50)
cuenta2.withdraw(80)