from tetris.entities.game import Game, EndOfGameException
import sys
import tty
import termios


def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def clear_screen():
    print "\033[H\033[J"


def main():

    game = Game()
    clear_screen()
    print game.current_board.render()

    actions = {'a': game.move_piece_left,
               'd': game.move_piece_right,
               'w': game.rotate_piece_right,
               's': game.rotate_piece_left,
               'x': game.move_piece_down,
               'e': exit}

    while True:
        command = getchar()
        if command in actions.keys():
            try:
                actions[command]()
                clear_screen()
                print game.current_board.render()
            except EndOfGameException:
                print "Game Over, Man! Game Over!"
                exit()


if __name__ == "__main__":
    main()
