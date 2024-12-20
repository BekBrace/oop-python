# Private attributes that you don't want to share across the program.
# Encapsulation

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        # Private attribute is created by adding __ to the variable's name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance

# Create a BankAccount object
account1 = BankAccount("John Doe", 1000)
print(f"User {account1.name} has the initial account balance of {account1.get_balance()}")  # Output: 1000

# account1.deposit(500)

deposit_amount = 500
updated_balance = account1.deposit(deposit_amount)
print(f"The updated balance of {account1.name} after depositing {deposit_amount} is {updated_balance}")  # Output: 1500
