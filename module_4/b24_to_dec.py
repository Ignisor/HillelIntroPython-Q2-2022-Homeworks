BASE = 24
CHAR_BASE = ord('A') - 1

print(f'Ласкаво просимо у конвертер системи числення з базою {BASE} в десяткову.')
print('Допустимі символи та їх значення:')
for i in range(BASE):
    if i < 10:
        print(f'{i} = {i}')
    else:
        print(f'{chr(CHAR_BASE + i - 9)} = {i}')

print()
inp_num = input(f'Введіть число в базі {BASE}: ').upper()

dec_value = 0
for i, char in enumerate(reversed(inp_num)):
    if char.isdigit():
        dec_value += int(char) * BASE ** i
    elif 9 < ord(char) - CHAR_BASE + 9 < BASE:
        dec_value += (ord(char) - CHAR_BASE + 9) * BASE ** i
    else:
        print('Введене число не відповідає базі.')
        dec_value = None
        break

if dec_value is not None:
    print(f'Ваше число в десятковій системі числення: {dec_value}')
