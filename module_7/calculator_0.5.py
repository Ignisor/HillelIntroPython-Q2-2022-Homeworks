from abc import ABC, abstractmethod


class Input:
    """
    Base class to handle user input and validation.
    In the base - no validations are implemented.
    """

    _ERROR = 'Помилка введення'

    def __init__(self, message='Будь ласка, введіть текст'):
        self.message = message

    def ask(self):
        return self._valid_input()

    def _valid_input(self):
        message = self.message + (': ' if not self.message.endswith(': ') else ' ')
        while True:
            inp = input(message)
            try:
                return self._validate(inp)
            except (ValueError, AssertionError):
                print(self._get_error())

    def _validate(self, inp):
        return inp

    def _get_error(self):
        return self._ERROR


class NumInput(Input):
    """Handle user input and validate it's a number"""

    _ERROR = 'Очікувалося число :/'

    def __init__(self, message='Будь ласка, введіть число'):
        super().__init__(message)

    def _validate(self, inp):
        return float(inp)


class MultiNumInput(NumInput):
    """
    Handle user input and validate it's a number.
    Repeat specified amount of time (if amount = '*' - until user input is empty).
    """

    def __init__(self, message='Будь ласка, введіть число', amount='*'):
        super().__init__(message)
        self._amount = amount

    def ask(self):
        inputs = []
        next_message = self.message + ' (введіть пустий рядок, щоб закінчити)'
        while self._amount == '*' or len(inputs) < self._amount:
            inp = self._valid_input()
            if inp is None:
                break
            inputs.append(inp)

            if self._amount == '*':
                self.message = next_message

        return inputs

    def _validate(self, inp):
        if self._amount == '*' and inp == '':
            return None

        return super()._validate(inp)


class Operation(ABC):
    """Abstract base class for executing operations"""

    INPUT_HANDLER = None
    SYMBOL = None

    def __init__(self):
        assert self.SYMBOL is not None

        self._operands = self._input()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def _input(self):
        assert self.INPUT_HANDLER is not None
        return self.INPUT_HANDLER.ask()

    @property
    @abstractmethod
    def result(self):
        raise NotImplementedError


class BinaryOperation(Operation, ABC):
    """Abstract base for binary operations (with two operands)"""

    INPUT_HANDLER = MultiNumInput(amount=2)

    def __init__(self):
        super().__init__()

        self._a, self._b = self._operands

    def __str__(self):
        return f'{self._a} {self.SYMBOL} {self._b}'


class Add(BinaryOperation):
    SYMBOL = '+'

    @property
    def result(self):
        return self._a + self._b


class Substract(BinaryOperation):
    SYMBOL = '-'

    @property
    def result(self):
        return self._a - self._b


class Multiply(BinaryOperation):
    SYMBOL = '*'

    @property
    def result(self):
        return self._a * self._b


class Divide(BinaryOperation):
    SYMBOL = '/'

    @property
    def result(self):
        try:
            return self._a / self._b
        except ZeroDivisionError:
            return '∞'


class MultiSum(Operation):
    """Sum any amount of numbers"""

    INPUT_HANDLER = MultiNumInput()
    SYMBOL = '+++'

    def __str__(self):
        return ' + '.join(map(str, self._operands))

    @property
    def result(self):
        return sum(self._operands)


OPERATIONS = (
    Add,
    Substract,
    Multiply,
    Divide,
    MultiSum,
)


class OperationSelect(Input):
    """Handle user input and validate it's valid operation"""

    def __init__(self):
        super().__init__(f'Будь ласка, оберіть операцію {list(self._operations_symbols)}')

    @property
    def _operations_symbols(self):
        return (operation.SYMBOL for operation in OPERATIONS)

    def _validate(self, inp):
        assert inp in self._operations_symbols
        return inp

    def _get_error(self):
        operations = ', '.join(self._operations_symbols)
        return f'Невідома операція. Можливі операції: {operations}'


class Calculator:
    """Main calculator logic"""

    WELCOME_MESSAGE = (
        'Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.5).\n'
        'Для тебе нічого не змінилося. Але я тепер серйозний 😎'
    )

    def execute(self):
        print(self.WELCOME_MESSAGE)

        operation = self._find_operation(OperationSelect().ask())
        operation = operation()

        print(f'{operation} = {operation.result}')

    def _find_operation(self, symbol):
        for operation in OPERATIONS:
            if operation.SYMBOL == symbol:
                return operation

        raise ValueError(f'Unknown operation {symbol}')


if __name__ == '__main__':
    calculator = Calculator()
    calculator.execute()
