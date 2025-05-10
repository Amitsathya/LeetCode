class Bank:

    def __init__(self, balance: List[int]):
        self.bankAccounts = {i + 1: balance[i] for i in range(len(balance))}
    
    def _is_valid_account(self, account: int) -> bool:
        return account in self.bankAccounts

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False
        if self.bankAccounts[account1] < money:
            return False
        self.bankAccounts[account1] -= money
        self.bankAccounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        self.bankAccounts[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        if self.bankAccounts[account] < money:
            return False
        self.bankAccounts[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)