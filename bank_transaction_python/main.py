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
class BankClient:
    def __init__(self, bank):
        self.bank = bank

    def open_acc_instruct(self):
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        balance = input("Enter initial Balance: ")
        acc = self.bank.OpenAccount(fname, lname, balance)
        print(acc)


    def get_choice(self, opt):
        return {
            "1": self.open_acc_instruct(),
            # '2': 2 ,
            # '3': 2 ,
            # '4': 2 ,
            # '5': 2 ,
            # '6': 2 ,
            # "7": sys.exit(),
        }.get(
            opt, print_instruct()
        )  # 9 is default if x not found


def main():
    b= Bank()
    bank_client = BankClient(b)
    while True:
        print_default_instruct()
        choice = input(f"{'Enter your choice: ':<25}")
        bank_client.get_choice(choice)


if __name__ == "__main__":
    main()