

class Account:
    MIN_BALANCE = 500
    NextAccountNumber = 0
    # private varible will be named with _ as prefix
    def __init__(self, fname="", lname="", balance=0):
        self._firstName = fname
        self._lastName = lname
        self._balance = balance
        Account.NextAccountNumber += 1
        self._accountNumber = Account.NextAccountNumber

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
            print("Not enough balance in this account")
            print(f"The minimum blance is {Account.MIN_BALANCE}")
            print(f'You only have {self._balance}')
        else:
            self._balance -= amount


    def setLastAccountNumber(self, accountNumber):
        Account.NextAccountNumber = accountNumber

    def getLastAccountNumber(self, accountNumber):
        return Account.NextAccountNumber

    def __str__(self):
        out = []
        out.append(f"{'Account Number' :<15}:{self.getAccNo() :>15}")
        out.append(f"{'First Name' :<15}:{self._firstName :>15}")
        out.append(f"{'Last Name' :<15}:{self._lastName :>15}")
        out.append(f"{'Balance' :<15}:{self.getBalance() :>15}")
        return "\n".join(out)

    def account_read(self, lines):
        self._accountNumber = int(lines.pop(0))
        self._firstName = lines.pop(0).strip()
        self._lastName = lines.pop(0).strip()
        self._balance = int(lines.pop(0).strip())

    def account_write(self, filename):
        f = open(filename, "a+")
        lines = f.readlines()
        lines.append(f"{self._accountNumber}\n")
        lines.append(f"{self._firstName}\n")
        lines.append(f"{self._lastName}\n")
        lines.append(f"{self._balance}\n")
        f.writelines(lines)
        f.close()

