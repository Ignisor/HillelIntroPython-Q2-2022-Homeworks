print('Добро пожаловать в НеВеРоЯтНыЙ калькулятор (версия 0.2)')
print('Теперь я умею складывать, отнимать, умножать и делить 2 любых целых числа 💪')
operation = input('Выберите операцию (+, -, *, /): ')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

result = None
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
else:
    print('Неизвестная операция', operation, 'выберите одно из: +, -, *, /')
    exit(1)

print(a, operation, b, '=', result)
