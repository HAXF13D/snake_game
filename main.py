from Game import Game
import os

game = Game()


while game.game_status:
    n = input()
    if n == 'U':
        game.move('UP')
        os.system('cls')
        game.print_field()
        game.print_field()
    if n == 'D':
        game.move('DOWN')
        os.system('cls')
        game.print_field()
        game.print_field()
    if n == 'L':
        game.move('LEFT')
        os.system('cls')
        game.print_field()
        game.print_field()
    if n == 'R':
        game.move('RIGHT')
        os.system('cls')
        game.print_field()
        game.print_field()
