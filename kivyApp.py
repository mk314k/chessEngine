"""
_summary_
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from chess import ChessBoard
import numpy as np
from utility import BUTTON_COLOR
from kivy.config import Config
     
Config.set('graphics', 'resizable', True)

class KButton(Button):
    def __init__(self,id, **kwargs):
        super().__init__(**kwargs)
        self.id =id

class mainGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        for i in range(64):
            button = KButton(id=i)
            button.bind(on_press=self.handleClick)
            button.background_color = BUTTON_COLOR[board[i][0]]
            if board[i][1]:
                button.background_normal ='img/' + str(board[i][1])+'.png'
                button.background_down = 'img/' +str(board[i][1])+'.png'
                button.background_color = (0,0.6,0.8,1)
            self.add_widget(button)

    def handleClick(self,instance:KButton):
        pass

class Chess(App):
    pass


if __name__ == '__main__':
    board = ChessBoard()
    board.startGame()
    app = Chess()
    app.run()