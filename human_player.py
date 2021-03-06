from board import Board, get_valid_moves, put_stone
from constants import HUMAN_PLAYER
from player import Player


class HumanPlayer(Player):

    def __init__(self, color):
        Player.__init__(self, color)
        self.type = HUMAN_PLAYER

    def play(self, board: Board, other_player):
        valid_moves = get_valid_moves(board.board, self.color)
        board.valid_moves = valid_moves
        print("BOARD", self.type, self.color)
        if not valid_moves:
            print('No more moves')
            return False
        print(board)
        while True:
            move = board.get_mouse_input()
            if move in valid_moves:
                print('Played move', move)
                new_board = put_stone(board.board, move, self.color)
                board.board = new_board
                break
        return True
