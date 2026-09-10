class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("El deposito debe ser mayor a 0")
        self.balance += amount
        return self.balance
        

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if amount > self.balance:
            raise RuntimeError("Fondos insuficientes")
        self.balance -= amount
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        if min_balance < 0:
            raise ValueError("El minimo no puede ser menor a 0")
        self.min_balance = min_balance
        super().__init__(balance)

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise PermissionError("Saldo por debajo del minimo")
        return super().withdraw(amount)

try:
    cuenta1 = BankAccount(100)
    print(f"Se creo cuenta de corriente con {cuenta1.balance} dolares")
    cuenta1.deposit(50)
    print(f'Nuevo saldo despues del deposito {cuenta1.balance} dolares')
    cuenta1.withdraw(25)
    print(f'Nuevo saldo despues del retiro {cuenta1.balance} dolares')
    cuenta1.withdraw(150)
    print(f'Nuevo saldo despues del retiro {cuenta1.balance} dolares')
except ValueError as e:
    print(f'Error: {e}')
except RuntimeError as e:
    print(f'Error: {e}')

try:
    cuenta2 = SavingsAccount(100, 25)
    print(f'Se creo cuenta de ahorros con {cuenta2.balance} dolores y un minimo de {cuenta2.min_balance} dolares')
    cuenta2.deposit(50)
    print(f'Nuevo saldo despues del deposito {cuenta1.balance} dolares')
    cuenta2.withdraw(50)
    print(f'Nuevo saldo despues del retiro {cuenta1.balance} dolares')
    cuenta2.withdraw(80)
    print(f'Nuevo saldo despues del retiro {cuenta1.balance} dolares')
except ValueError as e:
    print(f'Error: {e}')
except RuntimeError as e:
    print(f'Error: {e}')
except PermissionError as e:
    print(f'Error: {e}')