# tranform speed unit from Mile/h to Kilometer/h

class MovableAdapteeInterface:
    """
    Return speed mph
    """
    def GetSpeed( self ):
        pass

class RollsRoyce(MovableAdapteeInterface):
    
    def GetSpeed(self):
        return 155
    
#############################################################
class MovableTagetInterface:
    """
    Return speed kph
    """
    def GetSpeed(self):
        pass

class MovableAdapter(MovableTagetInterface):
    __adaptee = object
    
    def __init__( self, adaptee):
        self.__adaptee = adaptee
        
    def GetSpeed(self):
        return self.ConvertMPHtoKPH(self.__adaptee.GetSpeed())
    
    def ConvertMPHtoKPH( self, mph):
        return mph * 1.60934

car = RollsRoyce()
RollsRoyceAdapter = MovableAdapter(car)
RollsRoyceAdapter.GetSpeed()
print(RollsRoyceAdapter.GetSpeed())
