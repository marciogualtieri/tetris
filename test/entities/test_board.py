from unittest import TestCase
from tetris.entities.board import Board, InvalidPlacementException
from tetris.entities.piece import *


EMPTY_BOARD = ("*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "*                    *\n"
               "**********************")

FILLED_BOARD = ("*                    *\n"
                "*                    *\n"
                "*   *                *\n"
                "*   *                *\n"
                "*   **               *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "*                    *\n"
                "**********************")


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(20, 20)

    def test_create_empty_board(self):
        self.assertEqual(self.board.render(), EMPTY_BOARD)

    def test_place_piece_in_valid_position(self):
        self.board.place_piece(l_piece((2, 3)))
        self.assertEqual(self.board.render(), FILLED_BOARD)

    def test_place_piece_in_invalid_position(self):
        with self.assertRaises(InvalidPlacementException) as context:
            self.board.place_piece(l_piece((2, 3)))
            self.board.place_piece(l_piece((2, 3)))
        self.assertTrue("Can't move piece to coordinates (2, 3)." in context.exception)
