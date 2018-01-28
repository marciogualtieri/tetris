from tetris.entities.board import Board, InvalidPlacementException
from tetris.entities.piece import ALL_PIECES
from random import choice
from copy import deepcopy


class EndOfGameException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


class Game:

    def __init__(self, first_piece=choice(ALL_PIECES)()):
        self.background_board = Board(20, 20)
        self.current_board = Board(self.background_board.height, self.background_board.weight)
        self.piece = first_piece
        self.piece.coordinates = (0, self.current_board.weight / 2)
        self.current_board.place_piece(self.piece)

    def current_state(self):
        return self.current_board.render()

    def move_piece_left(self):
        self.__update_board_with_action__(self.piece.move_left)
        self.move_piece_down()

    def move_piece_right(self):
        self.__update_board_with_action__(self.piece.move_right)
        self.move_piece_down()

    def rotate_piece_left(self):
        self.__update_board_with_action__(self.piece.rotate_left)
        self.move_piece_down()

    def rotate_piece_right(self):
        self.__update_board_with_action__(self.piece.rotate_right)
        self.move_piece_down()

    def move_piece_down(self):
        self.__update_board_with_action__(self.piece.move_down)

    def __update_board_with_action__(self, action):
        piece_original_coordinates = self.piece.coordinates
        action()
        attempted_board = deepcopy(self.background_board)
        try:
            attempted_board.place_piece(self.piece)
            self.current_board = attempted_board
        except InvalidPlacementException:
            self.piece.coordinates = piece_original_coordinates
            if action.__name__ == "move_down":
                self.background_board = deepcopy(self.current_board)
                self.__create_new_piece__()

    def __create_new_piece__(self):
        self.piece = choice(ALL_PIECES)()
        self.piece.coordinates = (0, self.current_board.weight / 2)
        try:
            self.current_board.place_piece(self.piece)
        except InvalidPlacementException:
            raise EndOfGameException()
