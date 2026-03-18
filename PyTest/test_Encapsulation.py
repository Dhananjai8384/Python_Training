class Bank:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

def test_encapsulation():
    acc = Bank(5000)
    acc.deposit(2000)
    assert acc.get_balance() == 7000
