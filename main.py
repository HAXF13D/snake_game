class Field:

    def __init__(self):
        print("Введите количество строк")
        lines = int(input())
        self.lines = lines
        print("Введите количество столбцов")
        columns = int(input())
        self.columns = columns
        self.game_field = []
        self.__generate_field()
        self.food_line = 0
        self.food_column = 0
        self.generate_food()

    def __generate_field(self):
        for line in range(self.lines):

            temp_string = []
            for column in range(self.columns):
                if line == 0 or line == self.lines - 1 or column == 0 or column == self.columns - 1:
                    temp_string.append('#')
                else:
                    temp_string.append('.')

            self.game_field.append(temp_string)

    def generate_food(self):
        from random import randint
        if self.game_field[self.food_line][self.food_column] == '*':
            self.game_field[self.food_line][self.food_column] = '.'
            self.food_line = randint(1, self.lines - 2)
            self.food_column = randint(1, self.columns - 2)

        while self.game_field[self.food_line][self.food_column] != '.':
            self.food_line = randint(1, self.lines - 2)
            self.food_column = randint(1, self.columns - 2)
        self.game_field[self.food_line][self.food_column] = '*'


class Snake(Field):
    snake_pos = {}
    length = 1

    def set_snake(self):
        self.__generate_snake_pos()
        line_pos = self.snake_pos.get('line')[0]
        column_pos = self.snake_pos.get('column')[0]
        self.game_field[line_pos][column_pos] = '+'
        self.__generate_snake_pos()
        self.length = 1

    def __generate_snake_pos(self):
        from random import randint

        line = []
        column = []

        line.append(randint(1, self.lines - 2))
        column.append(randint(1, self.columns - 2))

        self.snake_pos['line'] = line
        self.snake_pos['column'] = column

    def print_pos(self):
        print(self.snake_pos.get('line'))
        print(self.snake_pos.get('column'))

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass


# def __generate_snake_pos(self):

class Game(Snake):
    player_field = ''

    def set_field(self):
        self.player_field = ''
        self.__generate_player_field()

    def __generate_player_field(self):
        self.player_field = ''
        for line in range(self.lines):
            for column in range(self.columns):
                self.player_field += self.game_field[line][column]
            self.player_field += '\n'

    def print_field(self):
        print(self.player_field)


game = Game()

