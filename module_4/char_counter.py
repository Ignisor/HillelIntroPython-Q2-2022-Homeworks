print('Привіт! Я тут щоб жувати жувачку та рахувати кількість символів у тексті 😎')
print('Як бачищ, жувати жувачку я не можу...')
text = input('Тож давай текст: ')

chars_count = {}
for char in text:
    chars_count[char] = chars_count.get(char, 0) + 1

for char, count in chars_count.items():
    print(f'- Символ "{char}" зустрічається {count} разів')
