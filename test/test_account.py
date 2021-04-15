import unittest
import sys
import os
from bank_transaction_python.lib.account import Account

class Item(unittest.TestCase):
    def test_constructor(self):
        acc = Account('andy','robert',5000)
        self.assertEqual(acc.getFirstName(),'andy')
        self.assertEqual(acc.getLastName(),'robert')
        self.assertEqual(acc.getBalance(),5000)
        acc = Account('andy','robert',400)
        self.assertEqual(acc.getFirstName(),'andy')
        self.assertEqual(acc.getLastName(),'robert')
        self.assertEqual(acc.getBalance(),400)
    
    def test_deposit(self):
        acc = Account('andy','yang',1000)
        acc.Deposit(500)
        self.assertEqual(acc.getBalance(),1500)
        acc.Deposit(500)
        self.assertEqual(acc.getBalance(),2000)

    def test_withdraw(self):
        acc = Account('andy','yang',1000)
        acc.WithDraw(500)
        self.assertEqual(acc.getBalance(),500)
        acc.WithDraw(100)
        # because 500 is the minimum Balance
        self.assertNotEqual(acc.getBalance(),400)
        self.assertEqual(acc.getBalance(),500)
    



if __name__ =='__main__':
    unittest.main()