import unittest
import sys
import os
import copy
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
    
    def test_setLastAccountNumber(self):
        acc = Account('andy','yang',1000)
        acc.setLastAccountNumber(10)
        self.assertEqual(10,acc.getLastAccountNumber())
        acc.setLastAccountNumber(100)
        self.assertEqual(100,acc.getLastAccountNumber())
        
    def test_account_write_read(self):
        # Write
        tesfile_name = 'account_write.data'
        acc = Account('andy','yang',1000)
        acc.account_write(tesfile_name)
        with open(tesfile_name) as f:
            f = f.readlines()
            self.assertEqual(int(f[-4]),acc.getLastAccountNumber())
            self.assertEqual(f[-3],acc.getFirstName()+'\n')
            self.assertEqual(f[-2],acc.getLastName()+'\n')
            self.assertEqual(int(f[-1]),acc.getBalance())
        acc2 = Account('brady','lin',2000)
        acc2.account_write(tesfile_name)
        with open(tesfile_name) as f:
            f = f.readlines()
            self.assertEqual(int(f[-4]),acc2.getLastAccountNumber())
            self.assertEqual(f[-3],acc2.getFirstName()+'\n')
            self.assertEqual(f[-2],acc2.getLastName()+'\n')
            self.assertEqual(int(f[-1]),acc2.getBalance())
        
        #Read
        with open(tesfile_name) as f:
            acclines = f.readlines()
            f2= f.readlines()
            orglines = copy.deepcopy(acclines) # after opne file, it could be opened only once
            acc_read = Account()
            acc_read.account_readlines(acclines)
            self.assertEqual(int(orglines[0]),acc_read.getAccNo())
            self.assertEqual(orglines[1],acc_read.getFirstName()+'\n')
            self.assertEqual(orglines[2],acc_read.getLastName()+'\n')
            self.assertEqual(int(orglines[3]),acc_read.getBalance())
            acc_read.account_readlines(acclines)
            self.assertEqual(int(orglines[4]),acc_read.getAccNo())
            self.assertEqual(orglines[5],acc_read.getFirstName()+'\n')
            self.assertEqual(orglines[6],acc_read.getLastName()+'\n')
            self.assertEqual(int(orglines[7]),acc_read.getBalance())
            



                

            

        

    



if __name__ =='__main__':
    unittest.main()