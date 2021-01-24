# DECORATOR PATTERN

class EmployeeComponentInterface:
    name = ''
    
    def getName(self):
        pass
    
    def doTask(self):
        pass
    
    def join( self, date):
        pass
    
class EmployeeConcreteComponent(EmployeeComponentInterface):
    
    name = ''
    
    def __init__( self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def join( self, joinDate):
        print(self.name + ' join on '+ joinDate)
    
    def terminate( self, terminateDate):
        print(self.name + ' terminate on '+ terminateDate)
        
    def doTask( self):
        print('do task')

class EmployeeDecorator(EmployeeComponentInterface):
    _employee = object
    
    def __init__( self, employee : EmployeeConcreteComponent):
        self._employee = employee
        
    def getName( self ):
        return self._employee.getName()
    
    def join( self, date):
        return self._employee.join(date)
    
    def terminate( self, date):
        return self._employee.terminate(date)
    
class Manager(EmployeeDecorator):
    
    def __init__(self, employee : EmployeeConcreteComponent):
        self._employee = employee
        
    def createRequirement(self):
        print(self._employee.getName() + " is create requirements.")
    
    def assignTask(self):
        print(self._employee.getName() + " is assigning tasks.")
    
    def managerProgress(self):
        print(self._employee.getName() + " is managering the progress")
    
    def doTask(self):
        self._employee.doTask()
        self.createRequirement()
        self.assignTask()
        self.managerProgress()
        
class teamLeader(EmployeeDecorator):
    
    def __init__( self,employee: EmployeeConcreteComponent):
        self._employee = employee
    
    def planing(self):
        print(self._employee.getName() + " is planing.")
    
    def motivate(self):
        print(self._employee.getName() + " is motivating his member.")

    def monitor(self):
        print(self._employee.getName() + " is monitoring his member.")

    def doTask(self):
        self._employee.doTask()
        self.planing()
        self.motivate()
        self.monitor()

class teamMember(EmployeeDecorator):
    
    def __init__( self, employee: EmployeeConcreteComponent):
        self._employee = employee
    
    def reportTask(self):
        print(self._employee.getName() + " is reporting his assigned task.")
    
    def coordinateWithOther( self ):
        print(self._employee.getName() + " is coordinating with other member.")
        
        

employee = EmployeeConcreteComponent('DNT')
employee.join('15-01-2021')
employee.terminate('20-01-2021')
manager = Manager(employee)
manager.createRequirement()