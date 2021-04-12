class InsufiicientFunds:
    pass


class Account:
    MIN_BALANCE = 500
    NextAccountNumber = 0
    # private varible will be named with _ as prefix
    def __init__(self, fname="", lname="", balance=0):
        Account.NextAccountNumber += 1
        self._accountNumber = Account.NextAccountNumber
        self._firstName = fname
        self._lastName = lname
        self._balance = balance

    def getAccNo(self):
        return self._accountNumber

    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def getBalance(self):
        return self._balance

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
        out = []
        out.append(f"First Name: {self._firstName}")
        out.append(f"Last Name: {self._lastName}")
        out.append(f"Account Number: {self.getAccNo()}")
        out.append(f"Balance: {self.getBalance()}")
        return "\n".join(out)

    def account_read(self, lines):
        self._accountNumber = lines.pop(0)
        self._firstName = lines.pop(0)
        self._lastName = lines.pop(0)
        self._balance = lines.pop(0)

    def account_write(self, filename):
        f = open(filename,'a')
        lines = f.readlines()
        lines.append(f"{self._accountNumber}\n")
        lines.append(f"{self._firstName}\n")
        lines.append(f"{self._lastName}\n")
        lines.append(f"{self._balance}\n")
        f.writelines(lines)
        f.close()
