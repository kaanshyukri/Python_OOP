class Account:

    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George")
print(account.credit(500))
print(account.debit(501))
print(account.info())

