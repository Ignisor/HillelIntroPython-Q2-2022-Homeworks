import math
import random
from typing import Generator, Optional


class Board:
    def __init__(self, size: int = 3):
        self._size = size
        self._board = [[' ' for _ in range(self._size)] for _ in range(self._size)]

    def __str__(self):
        """
        Render board to string like that:
          1 2 3
         ┏━┳━┳━┓
        A┃O┃X┃O┃
         ┣━╋━╋━┫
        B┃X┃O┃X┃
         ┣━╋━╋━┫
        C┃O┃X┃O┃
         ┗━┻━┻━┛
        """
        board_str = '  ' + ' '.join(map(str, range(1, self._size + 1))) + '\n'  # numbers row
        board_str += ' ┏' + '┳'.join('━' for _ in range(self._size)) + '┓\n'  # top border

        for i in range(self._size):
            board_str += f'{chr(i + ord("A"))}┃' + '┃'.join(self._board[i]) + '┃\n'
            if i < self._size - 1:
                board_str += ' ┣' + '╋'.join('━' for _ in range(self._size)) + '┫\n'
            else:
                board_str += ' ┗' + '┻'.join('━' for _ in range(self._size)) + '┛\n'  # bottom border

        return board_str

    def __getitem__(self, coordinates: str) -> str:
        y, x = self.coords_to_index(coordinates)
        return self._board[y][x]

    def __setitem__(self, coordinates: str, value: str):
        y, x = self.coords_to_index(coordinates)
        self._board[y][x] = value

    def __iter__(self) -> Generator[tuple[str, ...], None, None]:
        for row in self._board:
            yield tuple(row)

    @property
    def size(self) -> int:
        return self._size

    def find_all(self, value: str) -> Generator[str, None, None]:
        for y, row in enumerate(self._board):
            for x, cell in enumerate(row):
                if cell == value:
                    yield self.index_to_coords(y, x)

    def copy(self) -> 'Board':
        copy_board = self.__class__(self._size)
        copy_board._board = [list(row) for row in self]

        return copy_board

    @staticmethod
    def coords_to_index(coordinates: str) -> tuple[int, int]:
        assert len(coordinates) == 2, f'Invalid coordinates: {coordinates}'

        coordinates = coordinates.upper()

        x = None
        y = None

        for char in coordinates:
            if char.isdigit():
                x = int(char) - 1
            elif char.isalpha():
                y = ord(char) - ord('A')
            else:
                raise AssertionError(f'Invalid coordinates: {coordinates}')

        assert x is not None and y is not None, f'Invalid coordinates: {coordinates}'

        return y, x

    @staticmethod
    def index_to_coords(y: int, x: int) -> str:
        return f'{chr(y + ord("A"))}{x + 1}'


class XOXOGame:
    def __init__(self):
        self._board = Board()

    def __str__(self):
        str_ = 'XOXO'.center(4 + self._board.size * 2, '=') + '\n\n'  # title
        return str_ + str(self._board)

    @property
    def board(self) -> Board:
        return self._board

    def reset(self):
        self._board = Board()

    def make_move(self, move: str, player: str):
        try:
            assert self._board[move] == ' ', 'Invalid move, square is not empty'
            self._board[move] = player
        except IndexError:
            raise AssertionError(f'Invalid move, out of board')

    def check_win(self) -> Optional[str]:
        for player in ('X', 'O'):
            ys = []
            xs = []
            for coords in self._board.find_all(player):
                y, x = Board.coords_to_index(coords)
                ys.append(y)
                xs.append(x)

            for row in self._board:
                if row.count(player) == self._board.size:
                    return player

            for column in range(self._board.size):
                if [row[column] for row in self._board].count(player) == self._board.size:
                    return player

            if sum(x == y for x, y in zip(xs, ys)) == self._board.size:  # diagonal row from A1 to C3
                return player
            elif sum((2 - x) == y for x, y in zip(xs, ys)) == self._board.size:  # diagonal row from C3 to A1
                return player

        return None

    def copy(self):
        copy_game = self.__class__()
        copy_game._board = self._board.copy()

        return copy_game


class PlayerInterface:
    VALUE = 'X'

    def __init__(self, game: XOXOGame):
        self._game = game

    def make_move(self):
        while True:
            move = input('Enter your move: ')
            try:
                self._game.make_move(move, self.VALUE)
                break
            except AssertionError as e:
                print(e)


class ComputerInterface:
    VALUE = 'O'

    def __init__(self, game: XOXOGame):
        self._game = game

    def _minimax_move(self, game: XOXOGame, player: str) -> tuple[str, float]:
        """Minimax algorithm to find the best move"""
        best = ('', -math.inf if player == self.VALUE else math.inf)

        winner = game.check_win()
        if winner is not None:
            return ('', 1 if winner == self.VALUE else -1)

        possible_moves = list(game.board.find_all(' '))
        if len(possible_moves) == 0:
            return ('', 0)

        for move in possible_moves:
            copy_game = game.copy()
            copy_game.make_move(move, player)
            _, score = self._minimax_move(copy_game, 'O' if player == 'X' else 'X')

            if player == self.VALUE:
                if score > best[1]:
                    best = (move, score)
            else:
                if score < best[1]:
                    best = (move, score)

        return best

    def make_move(self):
        # if it's a first move in a game - don't think, just play randomly
        legit_moves = list(self._game.board.find_all(' '))
        if len(legit_moves) == self._game.board.size ** 2:
            move = random.choice(legit_moves)
        else:
            move, _ = self._minimax_move(self._game, self.VALUE)

        print(f'Computer move: {move}')
        self._game.make_move(move, self.VALUE)


if __name__ == '__main__':
    game = XOXOGame()
    player = PlayerInterface(game)
    computer = ComputerInterface(game)

    current = player if random.randint(0, 1) == 0 else computer

    while True:
        print(game)

        winner = game.check_win()
        if winner:
            print(f'{winner} wins!')
            break

        if len(list(game.board.find_all(' '))) == 0:
            print('Tie!')
            break

        current.make_move()
        print()

        current = computer if current == player else player
