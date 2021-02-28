import pygame

from ai_player import AIPlayer
from board import Board, score
from constants import WHITE_PLAYER, BLACK_PLAYER
from human_player import HumanPlayer
from random_player import RandomPlayer


class Othelo:
    board = None
    current_player = None

    def __init__(self):
        self.board = Board()
        self.players = [RandomPlayer(BLACK_PLAYER), AIPlayer(WHITE_PLAYER)]
        self.current_player = 0

    def next_player(self):
        self.current_player = (self.current_player + 1) % 2

    def play(self):
        other = self.players[(self.current_player + 1) % 2]
        if not self.players[self.current_player].play(self.board, other):
            return False
        self.players[0].score, self.players[1].score = score(self.board.board)
        self.next_player()
        if self.board.game_finished():
            return False
        return True

    def run(self):
        clock = pygame.time.Clock()
        pygame.display.flip()

        self.board.draw_score(self.players[0], self.players[1], self.players[self.current_player])
        self.board.setup()
        self.board.update()

        while True:
            if not self.play():
                print("Game finished")
                print(self.board)
                print("Score: ", score(self.board.board))
                break

            self.board.update()
            self.board.draw_score(self.players[0], self.players[1], self.players[self.current_player])
            clock.tick(60)
            pygame.display.flip()
        pass


if __name__ == '__main__':
    Othelo().run()
