print('Ласкаво просимо в шифрувальник/дешифрувальник для шифру Цезаря.')

action = input('Введіть "1" для шифрування, "2" для дешифрування: ').lower()
assert action in ('1', '2'), 'Невідома дія'

text = input('Введіть текст (тільки літери [a-z, A-Z]): ')
key = int(input('Введіть ключ: '))

result = ''

if action == '2':
    key = -key

for char in text:
    if ord('a') <= ord(char) <= ord('z'):
        char_shift = ord('a')
    elif ord('A') <= ord(char) <= ord('Z'):
        char_shift = ord('A')
    else:
        result += char
        continue

    result += chr(char_shift + (ord(char) - char_shift + key) % 26)

if result:
    print(f'Результат: {result}')
