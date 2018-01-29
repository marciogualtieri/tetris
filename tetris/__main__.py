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


def welcome_player():
    print ("\n\nWELCOME TO TETRIS!\n\n"
           "INSTRUCTIONS:\n\n"
           "    <A> - MOVE PIECE LEFT\n"
           "    <D> - MOVE PIECE RIGHT\n"
           "    <W> - ROTATE PIECE CLOCKWISE\n"
           "    <S> - ROTATE PIECE COUNTERCLOCKWISE\n"
           "    <X> - MOVE PIECE DOWN\n"
           "    <E> - EXIT THE GAME\n\n"
           "*** PRESS ANY KEY TO CONTINUE... ***")


def main():

    game = Game()
    welcome_player()
    getchar()
    clear_screen()
    print game.current_state()

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
                print "\nGAME OVER, MAN! GAME OVER!\n"
                exit()


if __name__ == "__main__":
    main()
