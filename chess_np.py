import numpy as np

BOARD_SIZE = 8
class ChessPiece():
    def __init__(self,colr,repr='E') -> None:
        self.__colr = colr
        self.__repr = repr
    def __repr__(self) -> str:
        return f'{self.__repr}{self.__colr}'
    def __str__(self) -> str:
        return self.__repr__()
    

class Rook(ChessPiece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(repr='R', *args, **kwargs)

class Bishop(ChessPiece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(repr='B', *args, **kwargs)

class King(ChessPiece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(repr='K', *args, **kwargs)

class Queen(ChessPiece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(repr='Q', *args, **kwargs)

class Knight(ChessPiece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(repr='N', *args, **kwargs)

class Pawn(ChessPiece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(repr='P', *args, **kwargs)
        self.__doubleStepForward = True

class ChessCell():
    def __init__(self, colr:COLOR, piece:ChessPiece|None = None) -> None:
        self.bgColr = colr
        self.piece = piece
        pass

class Color:
    BLACK = 0
    WHITE = 1

class Piece_Type:
    def __init__(self, colr=Color.black) -> None:
        self.pawn = 1

class Piece:
    PAWN = 1
    ROOK =2
    BISHOP = 3
    KNIGHT = 4
    QUEEN = 5
    KING = 6


class Chess_Board():
    def __init__(self, start_game=True) -> None:
        self.__board = np.zeros((3,BOARD_SIZE,BOARD_SIZE))
        for i in range(BOARD_SIZE):
            self.__board[0][i] = 
        if start_game:
            self.start_game()
            
    def __getitem__(self, index:tuple|int):
        if isinstance(index,int):
            cell:ChessCell = self.__board[index]
        else:
            cell:ChessCell = self.__board[index[0]*8+index[1]]
        return (cell.bgColr,cell.piece)

    def start_game(self):
        self.__board[0].piece = self.__board[7].piece = Rook(BLACK)
        self.__board[1].piece = self.__board[6].piece = Knight(BLACK)
        self.__board[2].piece = self.__board[5].piece = Bishop(BLACK)
        self.__board[3].piece = Queen(BLACK)
        self.__board[4].piece = King(BLACK)
        self.__board[56].piece = self.__board[63].piece = Rook(WHITE)
        self.__board[57].piece = self.__board[62].piece = Knight(WHITE)
        self.__board[58].piece = self.__board[61].piece = Bishop(WHITE)
        self.__board[59].piece = Queen(WHITE)
        self.__board[60].piece = King(WHITE)
    
    def showPath(self,index):
        """Returns all availabe path that can be taken by piece at given index

        Args:
            index ([type]): [description]
        """

        pass

    

    def __str__(self) -> str:
        pass


