from unittest import TestCase
from tetris.entities.piece import *


class TestPiece(TestCase):

    def test_create_piece(self):
        piece = Piece(("****\n"
                       "    \n"
                       "    \n"
                       "    "), (1, 2))
        self.assertEqual(piece.canvas, [["*", "*", "*", "*"],
                                        [" ", " ", " ", " "],
                                        [" ", " ", " ", " "],
                                        [" ", " ", " ", " "]])
        self.assertEqual(piece.coordinates, (1, 2))

    def test_rotate_piece_right(self):
        piece = stick_piece()
        piece.rotate_right()
        self.assertEqual(piece.canvas, [[" ", " ", " ", "*"],
                                        [" ", " ", " ", "*"],
                                        [" ", " ", " ", "*"],
                                        [" ", " ", " ", "*"]])

    def test_rotate_piece_left(self):
        piece = stick_piece()
        piece.rotate_left()
        self.assertEqual(piece.canvas, [["*", " ", " ", " "],
                                        ["*", " ", " ", " "],
                                        ["*", " ", " ", " "],
                                        ["*", " ", " ", " "]])

    def test_move_piece_right(self):
        piece = stick_piece((2, 2))
        piece.move_right()
        self.assertEqual(piece.coordinates, (2, 3))

    def test_move_piece_left(self):
        piece = stick_piece((2, 2))
        piece.move_left()
        self.assertEqual(piece.coordinates, (2, 1))

    def test_move_piece_down(self):
        piece = stick_piece((2, 2))
        piece.move_down()
        self.assertEqual(piece.coordinates, (3, 2))

    def test_stick_piece(self):
        self.assertEqual(stick_piece().canvas, [["*", "*", "*", "*"],
                                                [" ", " ", " ", " "],
                                                [" ", " ", " ", " "],
                                                [" ", " ", " ", " "]])

    def test_l_piece(self):
        self.assertEqual(l_piece().canvas, [["*", " ", " ", " "],
                                            ["*", " ", " ", " "],
                                            ["*", "*", " ", " "],
                                            [" ", " ", " ", " "]])

    def test_reverse_l_piece(self):
        self.assertEqual(reverse_l_piece().canvas, [[" ", "*", " ", " "],
                                                    [" ", "*", " ", " "],
                                                    ["*", "*", " ", " "],
                                                    [" ", " ", " ", " "]])

    def test_crank_piece(self):
        self.assertEqual(crank_piece().canvas, [[" ", "*", " ", " "],
                                                ["*", "*", " ", " "],
                                                ["*", " ", " ", " "],
                                                [" ", " ", " ", " "]])

    def test_square_piece(self):
        self.assertEqual(square_piece().canvas, [["*", "*", " ", " "],
                                                 ["*", "*", " ", " "],
                                                 [" ", " ", " ", " "],
                                                 [" ", " ", " ", " "]])
