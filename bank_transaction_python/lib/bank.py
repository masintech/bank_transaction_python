import os
from .account import Account


class Bank:
    def __init__(self, datafile_name="Bank.data"):
        self.datafile_name = datafile_name
        self.accounts = {}
        try:
            with open(self.datafile_name, "r+") as f:
                bank_data_lines = f.readlines()
                while bank_data_lines:
                    acc = Account()
                    acc.account_readlines(bank_data_lines)
                    if bank_data_lines: 
                        acc.setLastAccountNumber(acc.getAccNo())
                    self.accounts[acc.getAccNo()] = acc
        except IOError as error:
            print("Faile to open file Bank.data", error)

    def CloseAllAccounts(self):
        self.accounts = {}
        Account.NextAccountNumber = 0 

    def OpenAccount(self, fname, lname, balance):
        if balance >= Account.MIN_BALANCE:
            account = Account(fname, lname, balance)
            self.accounts[account.getAccNo()] = account
            account.account_write(self.datafile_name)
            return account
        else:
            print(f"The minum balance is {Account.MIN_BALANCE}")
            print("Open account rejected!!")
            return None

    def BalanceEquiry(self, accountNumber):
        # return the account class for displaying
        try:
            self.accounts[accountNumber]
        except KeyError as err:
            print("The account number doesn't exist ", err)
            return None
        else:
            return self.accounts[accountNumber]

    def Deposit(self, accountNumber, amount):
        try:
            self.accounts[accountNumber].Deposit(amount)
        except KeyError as err:
            print("The account number doesn't exist ", err)
        else:
            return self.accounts[accountNumber]

    def WithDraw(self, accountNumber, amount):
        try:
            self.accounts[accountNumber].WithDraw(amount)
        except KeyError as err:
            print("The account number doesn't exist ", err)
        return self.accounts[accountNumber]

    def CloseAccount(self, accountNumber):
        try:
            self.accounts.pop(accountNumber)
            self.ShowAllAccounts()
        except KeyError:
            print("The account number doesn't exist ")
            print("Plese check before doing it again!\n")

    def ShowAllAccounts(self):
        for key in self.accounts.keys():
            print(self.accounts[key])

    def __del__(self):
        with open(self.datafile_name, "w"):
            for account in self.accounts.values():
                account.account_write(self.datafile_name)
        print("Close with file written")
