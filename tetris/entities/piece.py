from numpy import matrix, rot90


class Piece:

    def __init__(self, shape, coordinates):
        self.canvas = [list(row) for row in shape.split("\n")]
        self.coordinates = coordinates

    def rotate_right(self):
        self.canvas = rot90(matrix(self.canvas), k=3).tolist()

    def rotate_left(self):
        self.canvas = rot90(matrix(self.canvas)).tolist()

    def move_right(self):
        (i, j) = self.coordinates
        self.coordinates = (i, j + 1)

    def move_left(self):
        (i, j) = self.coordinates
        self.coordinates = (i, j - 1)

    def move_down(self):
        (i, j) = self.coordinates
        self.coordinates = (i + 1, j)


def stick_piece(coordinates=(0, 0)):
    return Piece(("****\n"
                  "    \n"
                  "    \n"
                  "    "), coordinates)


def l_piece(coordinates=(0, 0)):
    return Piece(("*   \n"
                  "*   \n"
                  "**  \n"
                  "    "), coordinates)


def reverse_l_piece(coordinates=(0, 0)):
    return Piece((" *  \n"
                  " *  \n"
                  "**  \n"
                  "    "), coordinates)


def crank_piece(coordinates=(0, 0)):
    return Piece((" *  \n"
                  "**  \n"
                  "*   \n"
                  "    "), coordinates)


def square_piece(coordinates=(0, 0)):
    return Piece(("**  \n"
                  "**  \n"
                  "    \n"
                  "    "), coordinates)

ALL_PIECES = [stick_piece, l_piece, reverse_l_piece, crank_piece, square_piece]
