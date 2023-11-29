from Classes.view import View
from Classes.game import Game

if __name__ == '__main__':
    View.pycharm_info()
    while True:
        game = Game()
        game.start()
