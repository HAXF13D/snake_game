from Snake import Snake


class Game(Snake):
    _player_field = ''

    def __init__(self):
        super().__init__()
        self.print_field()

    def __set_field(self):
        self._player_field = ''
        self.__generate_player_field()

    def __generate_player_field(self):
        self._player_field = ''
        for line in range(self.lines):
            for column in range(self.columns):
                self._player_field += self._game_field[line][column]
            self._player_field += '\n'

    def print_field(self):
        self.__set_field()
        print(self._player_field)
