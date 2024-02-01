"""
_summary_

Returns:
    _type_: _description_
"""
BOARD_SIZE = 8

class Color:
    """
    _summary_
    """
    def __init__(self, value = "black"):
        self.value = value
    def flip(self):
        if self.value == 'black':
            return Color('white')
        else:
            return Color('black')
    def __repr__(self):
        return self.value

BLACK = Color()
WHITE = BLACK.flip()


class ChessPiece():
    """
    _summary_
    """
    def __init__(self,colr:Color, *args, **kwargs) -> None:
        self.__colr = colr
    def __repr__(self) -> str:
        return f'{self.__colr} {self.__class__.__name__}'
    def __str__(self) -> str:
        return self.__repr__()
    
# class Blank(Chess_Piece):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__()

class Rook(ChessPiece):
    """
    _summary_

    Args:
        Chess_Piece (_type_): _description_
    """
    def __init__(self, colr:Color, *args, **kwargs) -> None:
        super().__init__(colr, *args, **kwargs)


class Bishop(ChessPiece):
    def __init__(self, colr,  *args, **kwargs) -> None:
        super().__init__(colr, *args, **kwargs)

class King(ChessPiece):
    def __init__(self,colr, *args, **kwargs) -> None:
        super().__init__(colr, *args, **kwargs)

class Queen(ChessPiece):
    def __init__(self, colr, *args, **kwargs) -> None:
        super().__init__(colr, *args, **kwargs)

class Knight(ChessPiece):
    def __init__(self,colr, *args, **kwargs) -> None:
        super().__init__(colr, *args, **kwargs)

class Pawn(ChessPiece):
    """
    _summary_

    Args:
        ChessPiece (_type_): _description_
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__doubleStepForward = True
    def possible_moves(self):
        """

        Returns:
            _type_: _description_
        """


class ChessBoard:
    """
    _summary_
    """
    def __init__(self) -> None:
        self.__board = {}
        self.__board[0] = self.__board[7] = Rook(BLACK)
        self.__board[1] = self.__board[6] = Knight(BLACK)
        self.__board[2] = self.__board[5] = Bishop(BLACK)
        self.__board[3] = Queen(BLACK)
        self.__board[4] = King(BLACK)
        self.__board[56] = self.__board[63] = Rook(WHITE)
        self.__board[57] = self.__board[62] = Knight(WHITE)
        self.__board[58] = self.__board[61] = Bishop(WHITE)
        self.__board[59] = Queen(WHITE)
        self.__board[60] = King(WHITE)

        self.__chance = WHITE
    
    def show_path(self,index):
        """Returns all availabe path that can be taken by piece at given index

        Args:
            index ([type]): [description]
        """

        pass

    def __getitem__(self, index:tuple|int):
        if isinstance(index, tuple):
            index = index[0] * 8 + index[1]
        if index in self.__board:
            return self.__board[index]
        elif 0<=index<=63:
            return None
        raise KeyError

    def __str__(self) -> str:
        res = [f'{[self[i, j] for j in range(BOARD_SIZE)]}' for i in range(BOARD_SIZE)]
        return '\n'.join(res)


