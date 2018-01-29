class InvalidPlacementException(Exception):
    def __init__(self, piece):
        Exception.__init__(self, "Can't move piece to coordinates (%d, %d)." % piece.coordinates)


class Board:

    EMPTY_PIXEL = " "
    FILLED_PIXEL = "*"

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.canvas = [[self.__class__.EMPTY_PIXEL for _ in range(weight)] for _ in range(height)]

    def render(self):
        rendered_canvas = ""
        for i in range(0, self.height):
            rendered_canvas += self.__render_row__(self.canvas[i])
        rendered_canvas += self.__render_bottom__()
        return rendered_canvas

    def place_piece(self, piece):
        if self.__is_valid_placement__(piece):
            for i in range(0, len(piece.canvas)):
                for j in range(0, len(piece.canvas[0])):
                    if piece.canvas[i][j] == self.__class__.FILLED_PIXEL:
                        self.canvas[piece.coordinates[0] + i][piece.coordinates[1] + j] = piece.canvas[i][j]
        else:
            raise InvalidPlacementException(piece)

    def __render_row__(self, row):
        return self.__class__.FILLED_PIXEL + "".join(row) + self.__class__.FILLED_PIXEL + "\n"

    def __render_bottom__(self):
        return self.__class__.FILLED_PIXEL * (self.weight + 2)

    def __is_valid_placement__(self, piece):
        for i in range(0, len(piece.canvas)):
            for j in range(0, len(piece.canvas[0])):
                if piece.canvas[i][j] == self.__class__.FILLED_PIXEL \
                   and (not self.__inside_canvas__(piece, i, j) or self.__filled_pixel__(piece, i, j)):
                    return False
        return True

    def __inside_canvas__(self, piece, i, j):
        return 0 <= piece.coordinates[0] + i < self.weight and 0 <= piece.coordinates[1] + j < self.height

    def __filled_pixel__(self, piece, i, j):
        return self.canvas[piece.coordinates[0] + i][piece.coordinates[1] + j] == self.__class__.FILLED_PIXEL
