import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from account import Account


class Bank:
    def __init__(self):
        self.datafile_name = "Bank.data"
        self.accounts = {}
        try:
            with open(datafile_name) as f:
                bank_data_lines = f.readlines()
                while bank_data_lines:
                    acc = Account()
                    acc.account_read(bank_data_lines)
                    acc.setLastAccountNumber(acc.getAccNo())
                    self.accounts[acc.getAccNo()] = acc
        except IOError as error:
            print("Faile to open file Bank.data")

    def OpenAccount(self, fname, lname, balance):
        account = Account(fname, lname, balance)
        self.accounts[acc.getAccNo()] = account
        account.write_lines(datafile_name)
        return account

    def BalanceEquiry(self, accountNumber):
        # return the account class for displaying
        return self.accounts[accountNumber]

    def Deposit(self, accountNumber, amount):
        accounts[accountNumber].Deposit(amount)
        return self.accounts[accountNumber]

    def WithDraw(self, accountNumber, amount):
        account[accountNumber].WithDraw(amount)
        return self.accounts[accountNumber]

    def CloseAccount(self, accountNumber):
        self.accounts.pop(accountNumber)

    def ShowAllAccounts(self):
        for key in self.account.keys():
            print(self.accounts[key])

    def __del__(self):
        with open(self.datafile_name):
            for account in self.accounts:
                account.writelines(self.datafile_name)
        print("Close with file written")
