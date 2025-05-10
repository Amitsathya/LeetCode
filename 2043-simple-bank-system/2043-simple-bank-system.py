class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def isvalid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.isvalid(account1) and self.isvalid(account2) and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.isvalid(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.isvalid(account) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False