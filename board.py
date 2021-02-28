import copy
import sys
import time

import pygame
from pygame.locals import *
from constants import *


# noinspection DuplicatedCode
def get_valid_moves(board, current_player):
    other_player = BLACK_PLAYER if current_player == WHITE_PLAYER else WHITE_PLAYER
    player_stones = [(x, y) for x in range(TILES) for y in range(TILES) if board[x][y] == current_player]

    valid = []

    for (row, column) in player_stones:

        # up
        i = row - 1
        if i >= 0 and board[i][column] == other_player:
            i -= 1
            while i >= 0 and board[i][column] == other_player:
                i -= 1
            if i >= 0 and board[i][column] == EMPTY:
                valid += [(i, column)]

        # up-left
        i = row - 1
        j = column - 1
        if i >= 0 and j >= 0 and board[i][j] == other_player:
            i -= 1
            j -= 1
            while i >= 0 and j >= 0 and board[i][j] == other_player:
                i -= 1
                j -= 1
            if i >= 0 and j >= 0 and board[i][j] == EMPTY:
                valid += [(i, j)]

        # left
        j = column - 1
        if j >= 0 and board[row][j] == other_player:
            j -= 1
            while j >= 0 and board[row][j] == other_player:
                j -= 1
            if j >= 0 and board[row][j] == EMPTY:
                valid += [(row, j)]

        # left-down
        i = row + 1
        j = column - 1
        if i < TILES and j >= 0 and board[i][j] == other_player:
            i += 1
            j -= 1
            while i < TILES and j >= 0 and board[i][j] == other_player:
                i += 1
                j -= 1
            if i < TILES and j >= 0 and board[i][j] == EMPTY:
                valid += [(i, j)]

        # down
        i = row + 1
        if i < TILES and board[i][column] == other_player:
            i += 1
            while i < TILES and board[i][column] == other_player:
                i += 1
            if i < TILES and board[i][column] == EMPTY:
                valid += [(i, column)]

        # down-right
        i = row + 1
        j = column + 1
        if i < TILES and j < TILES and board[i][j] == other_player:
            i += 1
            j += 1
            while i < TILES and j < TILES and board[i][j] == other_player:
                i += 1
                j += 1
            if i < TILES and j < TILES and board[i][j] == EMPTY:
                valid += [(i, j)]

        # right
        j = column + 1
        if j < TILES and board[row][j] == other_player:
            j += 1
            while j < TILES and board[row][j] == other_player:
                j += 1
            if j < TILES and board[row][j] == EMPTY:
                valid += [(row, j)]

        # right-up
        i = row - 1
        j = column + 1
        if i >= 0 and j < TILES and board[i][j] == other_player:
            i -= 1
            j += 1
            while i >= 0 and j < TILES and board[i][j] == other_player:
                i -= 1
                j += 1
            if i >= 0 and j < TILES and board[i][j] == EMPTY:
                valid += [(i, j)]

    return list(set(valid))


def score(board):
    black, white = 0, 0
    for i in range(TILES):
        for j in range(TILES):
            if board[i][j] == BLACK_PLAYER:
                black += 1
            elif board[i][j] == WHITE_PLAYER:
                white += 1
    return black, white


def score_by_player(board, player):
    black, white = score(board)
    if player == WHITE_PLAYER:
        return white
    return black


def put_stone(board, position, player):
    board[position[0]][position[1]] = player
    new_board = flip_stones(board, position, player)
    return new_board


# noinspection DuplicatedCode
def flip_stones(board, move, current_player):
    other_player = BLACK_PLAYER if current_player == WHITE_PLAYER else WHITE_PLAYER
    row, column = move
    new_board = copy.deepcopy(board)

    incs = [(-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1)]

    # up
    i = row - 1
    places = []
    while i >= 0 and board[i][column] == other_player:
        places += [(i, column)]
        i -= 1
    if i >= 0 and board[i][column] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # up-left
    i = row - 1
    j = column - 1
    places = []
    while i >= 0 and j >= 0 and board[i][j] == other_player:
        places += [(i, j)]
        i -= 1
        j -= 1
    if i >= 0 and j >= 0 and board[i][j] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # left
    j = column - 1
    places = []
    while j >= 0 and board[row][j] == other_player:
        places += [(row, j)]
        j -= 1
    if j >= 0 and board[row][j] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # left-down
    i = row + 1
    j = column - 1
    places = []
    while i < TILES and j >= 0 and board[i][j] == other_player:
        places += [(i, j)]
        i += 1
        j -= 1
    if i < TILES and j >= 0 and board[i][j] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # down
    i = row + 1
    places = []
    while i < TILES and board[i][column] == other_player:
        places += [(i, column)]
        i += 1
    if i < TILES and board[i][column] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # down-right
    i = row + 1
    j = column + 1
    places = []
    while i < TILES and j < TILES and board[i][j] == other_player:
        places += [(i, j)]
        i += 1
        j += 1
    if i < TILES and j < TILES and board[i][j] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # right
    j = column + 1
    places = []
    while j < TILES and board[row][j] == other_player:
        places += [(row, j)]
        j += 1
    if j < TILES and board[row][j] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)

    # right-up
    i = row - 1
    j = column + 1
    places = []
    while i >= 0 and j < TILES and board[i][j] == other_player:
        places += [(i, j)]
        i -= 1
        j += 1
    if i >= 0 and j < TILES and board[i][j] == current_player:
        for place in places:
            new_board = put_stone(new_board, place, current_player)
    return new_board


class Board(pygame.Surface):
    board = None
    board_size = 0

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # Clear the screen
        self.screen.fill(BLACK)

        self.board_size = TILES * TILE_SIZE

        # Draw board
        pygame.Surface.__init__(self, (self.board_size, self.board_size))
        self.fill(DARK_GREY)
        for i in range(0, TILES):
            for j in range(0, TILES):
                pygame.draw.rect(self,
                                 GREY if (i + j) % 2 else DARK_GREY,
                                 (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        self.board = [[EMPTY for _ in range(0, TILES)] for _ in range(TILES)]
        print(self.board)
        self.screen.blit(self, (BOARD_LEFT, BOARD_TOP))
        self.draw_title()
        self.valid_moves = []

    def draw_title(self):
        title_fnt = pygame.font.SysFont("Times New Roman", 34)
        title = title_fnt.render("Othello", True, Color(255, 255, 255))
        title_pos = title.get_rect(
            centerx=SCORE_RIGHT / 2, centery=60)
        self.screen.blit(title, title_pos)

    def draw_score(self, black_player, white_player, current_player):
        print(black_player, white_player)
        default_color = Color(255, 0, 0)
        current_player_color = Color(0, 255, 0)

        fnt = pygame.font.SysFont("Times New Roman", 28)
        player1_txt_color = current_player_color if current_player.color == BLACK_PLAYER else default_color
        player1_txt = fnt.render("Black: " + str(black_player.score), True, player1_txt_color, Color(0, 0, 0))
        player1_pos = player1_txt.get_rect(
            centerx=SCORE_RIGHT / 2, centery=120)

        player2_txt_color = current_player_color if current_player.color == WHITE_PLAYER else default_color
        player2_txt = fnt.render("White: " + str(white_player.score), True, player2_txt_color, Color(0, 0, 0))
        player2_pos = player2_txt.get_rect(
            centerx=SCORE_RIGHT / 2, centery=150)

        self.screen.blit(player1_txt, player1_pos)
        self.screen.blit(player2_txt, player2_pos)

    def draw_tile(self, x, y, player_color):
        color = BLACK if player_color == BLACK_PLAYER else WHITE

        center_x = int(x * TILE_SIZE + (TILE_SIZE / 2))
        center_y = int(y * TILE_SIZE + (TILE_SIZE / 2))
        pygame.draw.circle(self, color, (center_x, center_y), int(0.8 * TILE_SIZE / 2))
        self.screen.blit(self, (BOARD_LEFT, BOARD_TOP))
        pygame.display.flip()

    def setup(self):
        self.board = put_stone(self.board, (3, 3), WHITE_PLAYER)
        self.board = put_stone(self.board, (3, 4), BLACK_PLAYER)
        self.board = put_stone(self.board, (4, 4), WHITE_PLAYER)
        self.board = put_stone(self.board, (4, 3), BLACK_PLAYER)

    def update(self):
        for i in range(0, TILES):
            for j in range(0, TILES):
                if self.board[i][j] != EMPTY:
                    # flip orientation to draw
                    self.draw_tile(j, i, self.board[i][j])

    def get_mouse_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if mouse_x < BOARD_LEFT or mouse_x > BOARD_LEFT + self.board_size \
                            or mouse_y < BOARD_TOP or mouse_y > BOARD_TOP + self.board_size:
                        continue

                    x = (mouse_x - BOARD_LEFT) // TILE_SIZE
                    y = (mouse_y - BOARD_TOP) // TILE_SIZE
                    # flip orientation
                    return y, x
                elif event.type == QUIT:
                    sys.exit(0)
            time.sleep(0.05)
        pass

    def game_finished(self):
        black, white = 0, 0
        for i in range(TILES):
            for j in range(TILES):
                if self.board[i][j] == BLACK_PLAYER:
                    black += 1
                elif self.board[i][j] == WHITE_PLAYER:
                    white += 1
        if black == 0:
            return WHITE_PLAYER
        elif white == 0:
            return BLACK_PLAYER
        return None

    def __str__(self):
        return print_board(self.board, self.valid_moves)

    def __repr__(self):
        return self.__str__()


def print_board(board, valid_moves=[]):
    string = ""
    string += '  | '
    for i in range(TILES):
        string += str(i) + ' | '
    string += '\n'
    for i in range(TILES):
        string += str(i) + ' |' + ' '
        for j in range(TILES):
            if board[i][j] == BLACK_PLAYER:
                string += 'B' + ' '
            elif board[i][j] == WHITE_PLAYER:
                string += 'W' + ' '
            elif (i, j) in valid_moves:
                string += 'x' + ' '
            else:
                string += ' ' + ' '
            string += '|' + ' '
        string += '\n'
    return string
