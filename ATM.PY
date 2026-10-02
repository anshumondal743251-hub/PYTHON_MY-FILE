class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("RS", amount, "debited")
        print("total balance", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("RS", amount, "credited")
        print("total balance", self.balance)

    def get_balance(self):
        print("total balance", self.balance)

acc1 = Account(10000, 123456)
acc1.debit(4000)
acc1.get_balance()


