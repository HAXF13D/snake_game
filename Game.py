from Snake import Snake
import pygame as pg

BLACK = (0, 0, 0)
GREEN = (173, 255, 47)
BLUE = (70, 130, 180)
RED = (220, 20, 60)
PINK = (255, 105, 180)
WHITE = (255, 255, 255)

WIDTH = 20
HEIGHT = 20

MARGIN = 1


class Game(Snake):
    _player_field = ''

    def __init__(self):
        super().__init__()
        # self.print_field(screen)
        self._SIZE = (self.columns * 21, self.lines * 21)
        pg.init()
        self._surface = pg.Surface(self._SIZE)
        self._screen = pg.display.set_mode(self._SIZE)
        pg.display.set_caption("Snake")
        self._clock = pg.time.Clock()
        self.__sp_status = 1
        self.__ai_state = 1

    def __draw(self):
        self._player_field = ''
        self._screen.fill(WHITE)
        for line in range(self.lines):
            for column in range(self.columns):
                color = BLACK
                if self._game_field[line][column] == self._BORDER_SIM:
                    color = PINK
                if self._game_field[line][column] == self._HEAD_SIM:
                    color = BLUE
                if self._game_field[line][column] == self._BODY_SIM:
                    color = GREEN
                if self._game_field[line][column] == self._FOOD_SIM:
                    color = RED
                pg.draw.rect(self._screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * line + MARGIN,
                              WIDTH,
                              HEIGHT])
                self._player_field += self._game_field[line][column]
            self._player_field += '\n'

    def run(self):
        direction = ''
        while self._game_status:
            self.__draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_w and self._last_move != 'D':
                        direction = 'UP'
                    if event.key == pg.K_s and self._last_move != 'U':
                        direction = 'DOWN'
                    if event.key == pg.K_a and self._last_move != 'R':
                        direction = 'LEFT'
                    if event.key == pg.K_d and self._last_move != 'L':
                        direction = 'RIGHT'
            self._move(direction)
            pg.display.flip()
            self._clock.tick(8)

    def __ai_start_pos(self, flag):
        result = ''
        if self.snake_pos['column'][0] == 1 and flag:
            result = 'RIGHT'
            flag = False
        elif self.snake_pos['line'][0] <= self.lines - 3:
            flag = False
            result = 'DOWN'
        elif self.snake_pos['column'][0] >= 2:
            result = 'LEFT'
            flag = False
        return result, flag

    def __spiral(self):
        result = ''
        if self.__ai_state == 1:
            if self.snake_pos['line'][0] == self.lines - 3 and self.snake_pos['column'][0] == self.columns - 2:
                result = 'DOWN'
                self.__ai_state = 2
            else:
                if self.__sp_status == 1:
                    if self.snake_pos['line'][0] >= 2:
                        result = 'UP'
                    else:
                        result = 'RIGHT'
                        self.__sp_status = 2

                elif self.__sp_status == 2:
                    if self.snake_pos['line'][0] == 2:
                        self.__sp_status = 3
                        result = 'DOWN'
                    else:
                        self.__sp_status = 3

                elif self.__sp_status == 3:
                    if self.snake_pos['line'][0] <= self.lines - 4:
                        result = 'DOWN'
                    else:
                        result = 'RIGHT'
                        self.__sp_status = 4

                elif self.__sp_status == 4:
                    if self.snake_pos['line'][0] == self.lines - 2:
                        self.__sp_status = 1
                        result = 'UP'
                    else:
                        self.__sp_status = 1

        print(result)
        return result

    def __back(self):
        result = ''
        if self.__ai_state == 2:
            if self.snake_pos['column'][0] >= 2:
                result = 'LEFT'
            else:
                self.__sp_status = 1
                self.__ai_state = 1
        return result

    def __ai(self):
        result = ''
        if self.__ai_state == 1:
            result = self.__spiral()
        else:
            result = self.__back()
        return result

    def ai_run(self):
        direction = ''
        flag_left = True
        flag_st = True
        while self._game_status:
            self.__draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            if flag_st:
                direction, flag_left = self.__ai_start_pos(flag_left)
                if self.snake_pos['line'][0] == self.lines - 2 and self.snake_pos['column'][0] == 1:
                    flag_st = False
            else:
                direction = self.__ai()
            # print(self._player_field)

            """   
            if self._last_move != 'D':
                direction = 'UP'
            if self._last_move != 'U':
                direction = 'DOWN'
            if self._last_move != 'R':
                direction = 'LEFT'
            if self._last_move != 'L':
                direction = 'RIGHT'
            """
            self._move(direction)
            pg.display.flip()
            self._clock.tick(120)
