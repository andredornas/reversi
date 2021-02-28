import math
import time

from board import Board, get_valid_moves, put_stone
from constants import AI_PLAYER
from minimax import minimax
from player import Player


class AIPlayer(Player):

    def __init__(self, color):
        Player.__init__(self, color)
        self.type = AI_PLAYER

    def play(self, board: Board, other_player):
        valid_moves = get_valid_moves(board.board, self.color)
        board.valid_moves = valid_moves
        print("BOARD", self.type, self.color)
        if not valid_moves:
            print('No more moves')
            return False
        print(board)
        time.sleep(0.5)
        start = time.time()
        score, new_board, move = minimax(board.board, 0, -math.inf, math.inf, self, other_player, self)
        board.board = new_board
        end = time.time()
        print('Played move', move)
        print('AI execution: ', end - start)
        time.sleep(0.5)
        # while True:
        #     move = board.get_mouse_input()
        #     if move in valid_moves:
        #         new_board = put_stone(board.board, move, self.color)
        #         board.board = new_board
        #         break
        return True
