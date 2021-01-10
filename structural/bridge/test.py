# module read file image for each OS
## Define kind of image file
class Extension:
    
    def preview(self):
        pass

class PNG(Extension):
    def preview(self):
        print('Read ' + self.__class__.__name__ + ' file')

class JPE(Extension):
    def preview(self):
        print('Read ' + self.__class__.__name__ + 'file')

## Define kind of OS

class Operation(object):
    _Extention = object
    
    def __init__( self, extention):
        self._Extention = extention
        
    def preview(self):
        pass

class WindowOS(Operation):
    def preview(self):
        self._Extention.preview()

class MacOS(Operation):
    def preview(self):
        self._Extention.preview()
        
img = PNG()
OS = WindowOS(img)
OS.preview()
