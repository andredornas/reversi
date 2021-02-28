from board import Board
from constants import BLACK_PLAYER, HUMAN_PLAYER


class Player:
    color = None
    type = None
    score = 0

    def __init__(self, color):
        self.color = color

    def play(self, board: Board, other_player):
        pass

    def __str__(self):
        color_text = "BLACK" if self.color == BLACK_PLAYER else "WHITE"
        type_text = "Human" if self.type == HUMAN_PLAYER else "AI"
        return "Player " + color_text + " (" + type_text + ") -> Score: " + str(self.score)

    def __repr__(self):
        return self.__str__()
