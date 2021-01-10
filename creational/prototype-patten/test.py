import copy 
<<<<<<< HEAD

class Cloneable:
    def clone(self):
        """
        Cloneable
        """
        if isinstance( self, object):
            return copy.deepcopy(self)
        else:
            print('the variable is not object')
            return None
        
class Computer(Cloneable):
    __os = ''
    __office = ''
    __antivirus = ''
    __browser = ''
    __others = ''
    
    def __init__( self, os = '', office = '', antivirus = '', browser = '', others = ''):
        self.__os = os
        self.__office = office
        self.__antivirus = antivirus
        self.__browser = browser
        self.__others = others
    
    def SetOthers( self, others):
        self.__others = others
        
    def GetInfo(self):
        print("Computer [os=" + self.__os + ", office=" + self.__office + ", antivirus=" + self.__antivirus + ", browser=" + self.__browser + ", others=" + self.__others + "]")
    
        
class Client:
    def __init__( self, **kwagrs):
        self.__computer = Computer(**kwagrs)
    
    def GetComputer(self):
        return self.__computer

test = Client(os = 'mac', office='microsolf', antivirus='bkav', browser='chrome', others='[cai gi do khac]').GetComputer()
test.GetInfo()

test2 = test.clone()

test2.SetOthers('[set cai other khac na]')
test2.GetInfo()


=======
>>>>>>> c41661ff6a643f0d50c1ea3c3eccc40b1e8e8e84
