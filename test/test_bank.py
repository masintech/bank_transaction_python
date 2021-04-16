import unittest
import copy
import os
from bank_transaction_python.lib.bank import Bank


class Item(unittest.TestCase):
    def test_constructor(self):
        bank = Bank()
        self.assertIsNotNone(bank)

    def test_close_all_accounts(self):
        bank = Bank()
        bank.CloseAllAccounts()
        self.assertDictEqual({}, bank.accounts)

    def test_open_account(self):
        bank = Bank()
        bank.CloseAllAccounts()
        bank.OpenAccount("default", "lastname", 5000)
        self.assertEqual(len(bank.accounts), 1)
        bank.OpenAccount("dd", "ee", 2000)
        self.assertEqual(len(bank.accounts), 2)
        bank.OpenAccount("ed", "fe", 2300)
        self.assertEqual(len(bank.accounts), 3)

    def test_bank_enquiry(self):
        bank = Bank()
        bank.CloseAllAccounts()
        bank.OpenAccount("default", "lastname", 5000)
        self.assertIsNotNone(bank.BalanceEquiry(1))
        self.assertIsNone(bank.BalanceEquiry(22))

    def test_deposit(self):
        bank = Bank()
        bank.CloseAllAccounts()
        acc = bank.OpenAccount("default", "lastname", 5000)
        acc = bank.Deposit(acc.getAccNo(), 500)
        self.assertEqual(5500, acc.getBalance())
        acc2 = bank.OpenAccount("dult", "laname", 5000)
        acc2 = bank.Deposit(acc2.getAccNo(), 500)
        self.assertEqual(5500, acc2.getBalance())

    def test_withdraw(self):
        bank = Bank()
        bank.CloseAllAccounts()
        acc = bank.OpenAccount("default", "lastname", 5000)
        acc = bank.WithDraw(acc.getAccNo(), 500)
        self.assertEqual(4500, acc.getBalance())
        acc2 = bank.OpenAccount("dult", "laname", 5000)
        acc2 = bank.WithDraw(acc2.getAccNo(), 500)
        self.assertEqual(4500, acc2.getBalance())

    def test_close_account(self):
        bank = Bank()
        bank.CloseAllAccounts()
        acc = bank.OpenAccount("default", "lastname", 5000)
        acc2 = bank.OpenAccount("talor", "lan", 600)
        bank.CloseAccount(acc2.getAccNo())
        self.assertIsNone(bank.BalanceEquiry(acc2.getAccNo()))

    def test_del_bank(self):
        bank = Bank()
        filename = bank.datafile_name
        del bank
        self.assertTrue(os.path.isfile(filename))
        
