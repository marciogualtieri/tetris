from unittest import TestCase
from tetris.entities.game import Game
from tetris.entities.piece import stick_piece


INITIAL_BOARD = ("*          ****      *\n"
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

MOVE_LEFT_BOARD = ("*                    *\n"
                   "*         ****       *\n"
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

MOVE_RIGHT_BOARD = ("*                    *\n"
                    "*           ****     *\n"
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

ROTATE_LEFT_BOARD = ("*                    *\n"
                     "*          *         *\n"
                     "*          *         *\n"
                     "*          *         *\n"
                     "*          *         *\n"
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

ROTATE_RIGHT_BOARD = ("*                    *\n"
                      "*             *      *\n"
                      "*             *      *\n"
                      "*             *      *\n"
                      "*             *      *\n"
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


class TestGame(TestCase):

    def setUp(self):
        self.game = Game(first_piece=stick_piece())

    def test_new_game(self):
        self.assertEqual(len(self.game.current_board.canvas), self.game.current_board.height)
        self.assertEqual(len(self.game.current_board.canvas[0]), self.game.current_board.weight)
        self.assertNotEqual(len(self.game.current_board.canvas), self.game.background_board.canvas)

    def test_move_piece_left(self):
        self.game.move_piece_left()
        self.assertEqual(self.game.current_board.render(), MOVE_LEFT_BOARD)

    def test_move_piece_right(self):
        self.game = Game(first_piece=stick_piece())
        self.game.move_piece_right()
        self.assertEqual(self.game.current_board.render(), MOVE_RIGHT_BOARD)

    def test_rotate_piece_left(self):
        self.game.rotate_piece_left()
        self.assertEqual(self.game.current_board.render(), ROTATE_LEFT_BOARD)

    def test_rotate_piece_right(self):
        print self.game.current_board.render()
        self.game.rotate_piece_right()
        print self.game.current_board.render()
        self.assertEqual(self.game.current_board.render(), ROTATE_RIGHT_BOARD)
