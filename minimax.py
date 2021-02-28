import copy
import math

from board import get_valid_moves, put_stone
from constants import TILES, EMPTY

MAX_DEPTH = 4


def evaluate(board, player):
    weights = [[120, 90, 60, 30, 30, 60, 90, 120],
               [ 90, 60, 30, 15, 15, 30, 60, 90],
               [ 60, 30, 15, 10, 10, 15, 30, 60],
               [ 30, 15, 10,  5,  5, 10, 15, 30],
               [ 30, 15, 10,  5,  5, 10, 15, 30],
               [ 60, 30, 15, 10, 10, 15, 30, 60],
               [ 90, 60, 30, 15, 15, 30, 60, 90],
               [120, 90, 60, 30, 30, 60, 90, 120]]

    s = 0
    for i in range(TILES):
        for j in range(TILES):
            if board[i][j] == player.color:
                s += weights[i][j]
            elif board[i][j] != player.color and board[i][j] != EMPTY:
                s -= weights[i][j]
    return s


def minimax(board, depth, alpha, beta, player, other_player, max_player):
    valid_moves = get_valid_moves(board, player.color)
    # print("Depth ", depth)
    if depth == MAX_DEPTH or not valid_moves:
        return evaluate(board, player), board, None

    if player.type == max_player.type:
        # print("Simulating AI Play")
        # print(print_board(board, valid_moves))
        best_val = -math.inf
        best_move = None
        best_child_board = None
        for move in valid_moves:
            new_board = put_stone(copy.deepcopy(board), move, player.color)
            # print('Move', move)
            child_score, new_board, _ = minimax(new_board, depth + 1, alpha, beta, other_player, player, max_player)
            # print('\t' * depth, 'Child from move ', move, ' - ', child_score)
            if child_score > best_val:
                best_val = child_score
                best_move = move
                best_child_board = new_board
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break
        return evaluate(best_child_board, player), best_child_board, best_move
    else:
        # print("Simulating Human Play")
        # print(print_board(board, valid_moves))
        best_val = math.inf
        best_move = None
        best_child_board = None
        for move in valid_moves:
            # print('Move', move)
            new_board = put_stone(copy.deepcopy(board), move, player.color)
            child_score, new_board, _ = minimax(new_board, depth + 1, alpha, beta, other_player, player, max_player)
            # print('\t' * depth, 'Child from move ', move, ' - ', child_score)
            if child_score < best_val:
                best_val = child_score
                best_move = move
                best_child_board = new_board
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return evaluate(best_child_board, player), best_child_board, best_move
