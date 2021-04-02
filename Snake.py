from Field import Field


class Snake(Field):
    snake_pos = {}
    __buf = '0'
    __last_move = '0'

    def __init__(self):
        super().__init__()
        self.__set_snake()
        self._generate_food()

    def __set_snake(self):
        self.__generate_snake_pos()
        line_pos = self.snake_pos.get('line')[0]
        column_pos = self.snake_pos.get('column')[0]
        self._game_field[line_pos][column_pos] = self._HEAD_SIM

    def __generate_snake_pos(self):
        from random import randint

        line = []
        column = []

        line.append(randint(1, self.lines - 2))
        column.append(randint(1, self.columns - 2))

        self.snake_pos['line'] = line
        self.snake_pos['column'] = column

    def __set_buf(self):
        x = self.snake_pos['line']
        y = self.snake_pos['column']

        if len(x) != 1:
            for i in range(len(x) - 1):
                if x[i] == x[i + 1]:
                    if y[i] == y[i + 1] - 1:
                        self.__buf = 'L'
                    else:
                        self.__buf = 'R'
                else:
                    if x[i] == x[i + 1] - 1:
                        self.__buf = 'U'
                    else:
                        self.__buf = 'D'

    def __grow(self):
        self.__set_buf()
        x = self.snake_pos['line']
        y = self.snake_pos['column']
        if self.__buf == 'U':
            x.append(x[len(x) - 1] + 1)
            y.append(y[len(y) - 1])

        if self.__buf == 'D':
            x.append(x[len(x) - 1] - 1)
            y.append(y[len(y) - 1])

        if self.__buf == 'L':
            x.append(x[len(x) - 1])
            y.append(y[len(y) - 1] + 1)

        if self.__buf == 'R':
            x.append(x[len(x) - 1])
            y.append(y[len(y) - 1] - 1)

        self._game_field[x[len(x) - 1]][y[len(y) - 1]] = self._BODY_SIM

        self.snake_pos['line'] = x
        self.snake_pos['column'] = y

    def __change_field(self, posx_1, posy_1, posx_2, posy_2, posx_3, posy_3):
        self._game_field[posx_1][posy_1] = self._HEAD_SIM
        self._game_field[posx_2][posy_2] = self._BODY_SIM
        self._game_field[posx_3][posy_3] = '.'

    def __check_collusion(self, posx, posy):
        if posx == self._food_line and posy == self._food_column:
            self.__grow()
            self._generate_food()
        if self._game_field[posx][posy] == '#' or self._game_field[posx][posy] == '+':
            self.game_status = False

    def move(self, direction):

        x = self.snake_pos['line']
        y = self.snake_pos['column']
        flag = True
        if direction == 'UP':
            if self.__last_move != 'D' or len(x) == 1:
                self.__buf = 'U'
                self.__last_move = 'U'
                flag = False
                self.__check_collusion(x[0] - 1, y[0])
                x.insert(0, x[0] - 1)
                y.insert(0, y[0])

        if direction == 'DOWN':
            if self.__last_move != 'U' or len(x) == 1:
                self.__buf = 'D'
                self.__last_move = 'D'
                flag = False
                self.__check_collusion(x[0] + 1, y[0])
                x.insert(0, x[0] + 1)
                y.insert(0, y[0])

        if direction == 'RIGHT':
            if self.__last_move != 'L' or len(x) == 1:
                self.__buf = 'R'
                self.__last_move = 'R'
                flag = False
                self.__check_collusion(x[0], y[0] + 1)
                x.insert(0, x[0])
                y.insert(0, y[0] + 1)

        if direction == 'LEFT':
            if self.__last_move != 'R' or len(x) == 1:
                self.__buf = 'L'
                self.__last_move = 'L'
                flag = False
                self.__check_collusion(x[0], y[0] - 1)
                x.insert(0, x[0])
                y.insert(0, y[0] - 1)

        if not flag:
            temp_x = x[len(x) - 1]
            temp_y = y[len(y) - 1]

            if not flag:

                x.pop(len(x) - 1)
                y.pop(len(y) - 1)

            self.snake_pos['line'] = x
            self.snake_pos['column'] = y

            if len(x) != 1:
                self.__change_field(x[0], y[0], x[1], y[1], temp_x, temp_y)
            else:
                self.__change_field(x[0], y[0], temp_x, temp_y, temp_x, temp_y)
