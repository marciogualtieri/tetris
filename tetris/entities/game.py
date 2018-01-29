from tetris.entities.board import Board, InvalidPlacementException
from tetris.entities.piece import ALL_PIECES
from random import choice
from copy import deepcopy


class EndOfGameException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Game:

    def __init__(self, first_piece=None):
        self.background_board = Board(20, 20)
        self.current_board = Board(self.background_board.height, self.background_board.weight)
        self.__place_new_piece__(first_piece)

    def current_state(self):
        return self.current_board.render()

    def move_piece_left(self):
        self.__update_board_with_action__(action=self.piece.move_left,
                                          recovery_actions=[self.piece.rollback])
        self.move_piece_down()

    def move_piece_right(self):
        self.__update_board_with_action__(action=self.piece.move_right,
                                          recovery_actions=[self.piece.rollback])
        self.move_piece_down()

    def rotate_piece_left(self):
        self.__update_board_with_action__(action=self.piece.rotate_left,
                                          recovery_actions=[self.piece.rollback])
        self.move_piece_down()

    def rotate_piece_right(self):
        self.__update_board_with_action__(action=self.piece.rotate_right,
                                          recovery_actions=[self.piece.rollback])
        self.move_piece_down()

    def move_piece_down(self):
        self.__update_board_with_action__(action=self.piece.move_down,
                                          recovery_actions=[self.piece.rollback, self.reset_board])

    def __update_board_with_action__(self, action, recovery_actions):
        action()
        attempted_board = deepcopy(self.background_board)
        try:
            attempted_board.place_piece(self.piece)
            self.current_board = attempted_board
        except InvalidPlacementException:
            [recovery_action() for recovery_action in recovery_actions]

    def reset_board(self):
        self.background_board = deepcopy(self.current_board)
        self.__place_new_piece__()

    def __place_new_piece__(self, piece=None):
        self.piece = choice(ALL_PIECES)() if piece is None else piece
        self.piece.coordinates = (0, self.current_board.weight / 2)
        try:
            self.current_board.place_piece(self.piece)
        except InvalidPlacementException:
            raise EndOfGameException()
