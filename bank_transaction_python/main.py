from lib.bank import Bank
from lib.account import Account
import sys


def print_instruct():
    print(f"{'*****Banking System*****':^25}")
    print(f"{'Select one option below':<25}")
    print(f"{'1 Open an Account':<25}")
    print(f"{'2 Balance Enquiry':<25}")
    print(f"{'3 Deposit':<25}")
    print(f"{'4 Withdrawal':<25}")
    print(f"{'5 Close an Account':<25}")
    print(f"{'6 Show All Accounts':<25}")
    print(f"{'7 Quit':<25}")


def print_default_instruct():
    print("Please enter correct choice:")

def check_numeric_input(input):
    try:
        # integer is an acceptable data type
        val = int(input)
    except ValueError:
        try:
            # float is the other acceptable data type 
            val = float(input)
        except ValueError:
            print("Input must be numeric!")
            print("Please try again!!")
            return False
    return True

        

class BankClient:
    def __init__(self, bank):
        self.bank = bank

    def open_acc_instruct(self):
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        balance = input("Enter initial Balance: ")
        if check_numeric_input(balance):
            acc = self.bank.OpenAccount(fname.strip(), lname.strip(), balance)
            print(acc)

    def balance_enquiry(self):
        accountNumber = input("Enter Account Number")
        acc = self.bank.BalanceEquiry(accountNumber)
        print(f"Your Account Details: {acc}")

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def close_account(self):
        pass

    def show_all_accounts(self):
        for account in self.bank.accounts.values():
            print(account)
            print('\n')

    def quit_system(self):
        del self.bank
        sys.exit()

    def get_choice(self, opt):
        funct= {
            "1": self.open_acc_instruct,
            "2": self.balance_enquiry,
            "3": self.deposit,
            "4": self.withdraw,
            "5": self.close_account,
            "6": self.show_all_accounts,
            "7": self.quit_system,
        }.get(
            opt, print_default_instruct
        )  # 9 is default if x not found
        funct()


def main():
    b = Bank()
    bank_client = BankClient(b)
    choice = 0
    while choice!=7:
        print_instruct()
        choice = input(f"{'Enter your choice: ':<25}")
        print(f'Your choose {choice}')
        bank_client.get_choice(choice)
        print('\n')


if __name__ == "__main__":
    main()