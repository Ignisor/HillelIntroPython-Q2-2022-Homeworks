print('Ласкаво просимо до ЧуДоВоГо калькулятору (версія 0.3)')
print('Тепер я також вмію швидко складати багато чисел. Спробуй нову операцію "+++" 😉')
operation = input('Оберіть операцію (+, -, *, /, +++): ')

if operation in ('+', '-', '*', '/'):
    a = int(input('Введіть перше число: '))
    b = int(input('Введіть друге число: '))
elif operation in ('+++',):
    print('Введіть декілька чисел, по заверщенню залиште строку пустою')
    nums = []
    input_str = True

    while input_str:
        input_str = input(
            'Введіть число та натисніть Enter (якщо бажаете завершити, просто натисніть Enter):'
        )
        if input_str:
            nums.append(int(input_str))

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
else:
    print('Невідома операція', operation, 'оберіть одне з: +, -, *, /, +++')

if result is not None:
    print('Результат:', result)
