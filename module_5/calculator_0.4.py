def input_num(message='Введіть число: ', allow_empty=False):
    while True:
        inp_ = input(message)

        if inp_ == '' and allow_empty:
            return inp_

        try:
            return float(inp_)
        except ValueError:
            print('Це не число. Спробуйте ще раз.')


print('Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.4)')
print('Тепер я вмію працювати з будь-якими числами, а також перевіряю введені дані.')
operation = input('Оберіть операцію (+, -, *, /, +++): ')

if operation in ('+', '-', '*', '/'):
    a = input_num('Введіть перше число: ')
    b = input_num('Введіть друге число: ')
elif operation in ('+++',):
    print('Введіть декілька чисел, по завершенню залиште строку пустою')
    nums = []
    input_str = True

    while input_str:
        input_str = input_num(
            'Введіть число та натисніть Enter (якщо бажаете завершити, просто натисніть Enter): ',
            allow_empty=True,
        )
        if input_str:
            nums.append(int(input_str))
else:
    print('Невідома операція', operation, 'оберіть одне з: +, -, *, /, +++')


result = None
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif operation == '+++':
    result = sum(nums)

if result is not None:
    print('Результат:', result)
