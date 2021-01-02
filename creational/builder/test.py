def empty(value):
    try:
        value = float(value)
    except ValueError:
        pass
    return bool(value)

class accountBuilderInterface:
    
    def setAccountNumber(self, accountNumber):
        pass
    
    def setOwner( self, owner):
        pass
    
    def setBranch( self, branch):
        pass
    
    def setBalance( self, balance):
        pass
    
    def setInterestRate( self, interestRate):
        pass
    
    def build(self):
        pass
    
class bankAccountBuilder(accountBuilderInterface):
    __accountNumber = 0
    __owner = ''
    __branch = ''
    __balance = 0
    __interestRate = 0
        
    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber
        return self
    
    def setOwner( self, owner):
        self.__owner = owner
        return self
    
    def setBranch( self, branch):
        self.__branch = branch
        return self
    
    def setBalance( self, balance):
        self.__balance = balance
        return self
    
    def setInterestRate( self, interestRate):
        self.__interestRate = interestRate
        return self
    
    def build(self):
        return bankAccount( accountNumber = self.__accountNumber, 
                           owner = self.__owner, 
                           branch = self.__branch,
                           interestRate = self.__interestRate,
                           balance = self.__balance)
    
class bankAccount:
    __accountNumber = 0
    __owner = ''
    __branch = ''
    __balance = 0
    __interestRate = 0
        
    def __init__( self, accountNumber = None, owner = None, branch= None, balance = 0, interestRate = None):
        self.__accountNumber = accountNumber
        self.__owner = owner
        self.__branch = branch
        self.__balance = balance
        self.__interestRate = interestRate
        
    def getAccountNumber(self):
        return self.__accountNumber
    
    def getOwner(self):
        return self.__owner
    
    def getBranch(self):
        return self.__branch
    
    def getBalance(self):
        return self.__balance
    
    def getInterestRate(self):
        return self.__interestRate
    
    def getInfo(self):
        print("XYZ Bank – Account Information")
        print("\n")
        
        if  self.__accountNumber:
            print('account number: ')
            print(self.__accountNumber)
            print("\n")
            
        if  self.__owner:
            print('owner: ')
            print(self.__owner)
            print("\n")
            
        if  self.__branch:
            print('branch: ')
            print(self.__branch)
            print("\n")
        
        if  self.__balance:
            print('balance: ')
            print(self.__balance)
            print("\n")
        
        if  self.__interestRate:
            print('interest rate: ')
            print(self.__interestRate)
            print("\n")
            
test = bankAccountBuilder()
test.setAccountNumber(123321)
test.setOwner('XthanhX')
test.setBranch('hcm')
test.setInterestRate(2.5)
# test = test.build()

# test.getInfo()
# print(test.getBranch())

import copy
from pprint import pprint

test1 = copy.deepcopy(test)
pprint(dir(test1))
# print(test1.__dict__)





