#============ bank =======================

class bank:
    
    def getName(self):
        pass
    
class vietComBank(bank):
    def getName(self):
        return 'vietCombank'

class VPBank(bank):
    def getName(self):
        return 'VPBank'
    
#============= factory ==============

class factoryBank:
    def __init__(self, type):
        self.type = type
    
    def getbank(self):
        getBank = {
            'vietComBank': vietComBank(),
            'VPBank'     : VPBank()
        }
        
        return getBank.get(self.type,"bank haven't in system")
#============= client ==============
class client:
    def __init__(self,bank):
        self.typeBank = factoryBank(bank)
        
    def bank(self):
        return self.typeBank.getbank()


test = client('VPBank')
bank = test.bank()
bank = bank.getName()
print(bank)