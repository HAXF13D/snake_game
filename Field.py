class Field:

    _EMPTY_SIM = '.'
    _BORDER_SIM = '#'
    _FOOD_SIM = '*'
    _HEAD_SIM = '@'
    _BODY_SIM = '+'

    def __init__(self):
        print("Введите количество строк")
        lines = int(input())
        self.lines = lines
        print("Введите количество столбцов")
        columns = int(input())
        self.columns = columns
        self._game_field = []
        self.__generate_field()
        self._food_line = 0
        self._food_column = 0
        self._game_status = True

    def __generate_field(self):
        for line in range(self.lines):

            temp_string = []
            for column in range(self.columns):
                if line == 0 or line == self.lines - 1 or column == 0 or column == self.columns - 1:
                    temp_string.append(self._BORDER_SIM)
                else:
                    temp_string.append(self._EMPTY_SIM)

            self._game_field.append(temp_string)

    def __check_food(self):
        result = False
        for line in range(self.lines):
            for column in range(self.columns):
                if self._game_field[line][column] == self._FOOD_SIM:
                    result = True
        return result

    def _generate_food(self):
        if not self.__check_food():
            from random import randint
            while self._game_field[self._food_line][self._food_column] != self._EMPTY_SIM:
                self._food_line = randint(1, self.lines - 2)
                self._food_column = randint(1, self.columns - 2)
            self._game_field[self._food_line][self._food_column] = self._FOOD_SIM
