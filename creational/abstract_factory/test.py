#============= furniture ===============

class chairInterface:
    def create(self):
        pass

class TableInterface:
    def create(self):
        """
        create table
        """
        pass

#============== procedure ==============
# chair
class plasticChair(chairInterface):
    def create(self):
        return 'plastic chair'

class woodChair(chairInterface):
    def create(self):
        return 'wood chair'
    
# table

class plasticTable(TableInterface):
    def create(self):
        return 'plastic table'

class woodTable(TableInterface):
    def create(self):
        return 'wood table'

#============== type factory ================
# factory interface

class factoryInterface:
    def table(self):
        """
        create Tabe
        """
        pass
    def chair(self):
        """
        create chair
        """
        pass
# facrory

class plasticFacroty(factoryInterface):
    """
    plastic factory procedure
    """
    def table(self):
        """
        create plastic table
        """
        return plasticTable()
    
    def chair(self):
        """
        create plastic chair
        """
        return plasticChair()
    
class woodFacroty(factoryInterface):
    """
    wood factory procedure
    """
    def table(self):
        """
        create plastic table
        """
        return woodTable()
    
    def chair(self):
        """
        create plastic chair
        """
        return woodChair()
    
#==================  furniture abstract factory =========================

class furnitureAbstractFactory:
    def getFactory(self, type):
        
        allFactory= {
            'wood'      : woodFacroty(),
            'plastic'   : plasticFacroty()
        }
        
        return allFactory.get(type,"factory haven't in system")
        
class client:
    def __init__(self, type):
        self.type = type
    
    def getTypeFurniture(self):
        return furnitureAbstractFactory().getFactory(self.type)

test = client('wood')
test = test.getTypeFurniture()
test = test.table().create()
print(test)