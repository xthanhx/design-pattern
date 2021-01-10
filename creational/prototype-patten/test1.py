import copy
from typing import Final
import time
start_time = time.time()


class Cells:
    def GetCell( self, color):
        return '[ ' + color + ' ]'
    def Cloneable( self):
        return copy.deepcopy(self)
    
class board:
    COL: Final = 8
    CELL: Final = 8
    def FrameBoard(self):
        col = self.COL
        cell = self.CELL
        i = 0
        e = 0
        Cell = Cells().Cloneable()
        board = {}
        
        for i in range(col):
            boardCell = {}
            for e in range(cell):
                if ( i + e ) % 2 == 0:
                    square = 'WHITE'
                else:
                    square = 'BLACK'
                    
                boardCell[e] = Cell.GetCell(square)
                
            board[i] = boardCell
            i +=1
        
        self.board = board
        
    def paintBoard(self):
        board = self.board
        cell = ''
        for key in board:
    
            col = ''
            cell = board[key]
            for x in cell:
                col += (cell[x])
            print(col)
            


test = board()
test.FrameBoard()
test.paintBoard()


print("--- %s seconds ---" % (time.time() - start_time))