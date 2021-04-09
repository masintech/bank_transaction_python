class InsufiicientFunds:
    pass


class Account:
    MIN_BALANCE = 500
    NextAccountNumber = 0
    # private varible will be named with _ as prefix
    def __init__(self, fname, lname, balance, NextAccountNumber):
        NextAccountNumber += 1
        self._accountNumber = NextAccountNumber
        self._firstName = fname
        self._lastName = lname
        self._balance = balance

    def Deposit(self, amount):
        self._balance += amount

    def WithDraw(self, amount):
        if self._balance - amount < Account.MIN_BALANCE:
            raise InsufiicientFunds
        self._balance -= amount

    def setLastAccountNumber(self, accountNumber):
        Account.NextAccountNumber = accountNumber

    def getLastAccountNumber(self, accountNumber):
        return Account.NextAccountNumber
    
    