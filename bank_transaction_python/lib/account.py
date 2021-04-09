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

    def getFirstName(self):
        return _firstName

    def getLastName(self):
        return _lastName

    def getBalance(self):
        return _balance

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

    def __str__(self):
        print(self._accountNumber)
        print(self._firstName)
        print(self._lastName)
        print(self._balance)
    
    def account_write(self):
        write_lines=[]
        write_lines.append(f'First Name: {self._firstName}')
        write_lines.append(f'Last Name: {self._lastName}')
        write_lines.append(f'Account Number: {self.getAccNo()')
        write_lines.append(f'Balance: {self.getBalance()}')
        return write_lines
         
         
