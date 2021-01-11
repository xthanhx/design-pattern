# Manager forder and file
# Interface 
class FileComponentInterface:
    
    def ShowProperty(self):
        pass
    
    def TotalSize(self):
        pass

class FileLeaf(FileComponentInterface):
    
    def __init__(self, name: str, size : int):
        self.name = name
        self.size = size

    def TotalSize(self):
        return self.size
    
    def ShowProperty(self):
        print('[name: '+ self.name + ' | size: ' + str(self.size) + ' ]')
    
class FolderComposite(FileComponentInterface):
    
    listfile = []
    
    def __init__(self, files: list):
        self.listfile = files
    
    def ShowProperty(self):
        for file in self.listfile:
            file.ShowProperty()
    
    def TotalSize(self):
        
        total = 0
        
        for file in self.listfile:
            total += file.TotalSize()
            
        return total
    

file1 =  FileLeaf( 'file1', 80)
file2 =  FileLeaf( 'file2', 70)
file3 =  FileLeaf( 'file3', 90)

allFile = [ file1, file2, file3]

folder = FolderComposite(files = allFile)
folder.ShowProperty()
print(folder.TotalSize())