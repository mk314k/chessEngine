from utility import BOARD_SIZE, BLACK, WHITE, COLOR_TYPE

class ChessPiece():
    def __init__(self,colr:COLOR_TYPE) -> None:
        self.__colr = colr
        
        pass

class Rook(ChessPiece):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class Bishop(ChessPiece):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class King(ChessPiece):
    def __init__(self) -> None:
        super().__init__()

class Queen(ChessPiece):
    def __init__(self) -> None:
        super().__init__()

class Knight(ChessPiece):
    def __init__(self) -> None:
        super().__init__()

class Pawn(ChessPiece):
    def __init__(self) -> None:
        super().__init__()

class ChessCell():
    def __init__(self, colr:COLOR_TYPE, piece:ChessPiece|None = None) -> None:
        self.__colr = colr
        self.__piece = piece
        pass

    def _ChessBoard__change(self, newPiece:ChessPiece|None):

        pass


class ChessBoard():
    def __init__(self) -> None:
        self.__board = [None]*BOARD_SIZE**2
        for i in range(0,BOARD_SIZE**2,2):
            self.__board[i] = ChessCell(BLACK)
            self.__board[i+1] = ChessCell(WHITE)
    
    def showPath(self,index):
        """Returns all availabe path that can be taken by piece at given index

        Args:
            index ([type]): [description]
        """

        pass

    def __getitem__(self, index:int):
        return self.__board[index]


