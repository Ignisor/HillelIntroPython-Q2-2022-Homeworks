print('Вас приветствует конвертер смайликов в емоджи 🙂😂🙁😠😈')
text = input('Введите текст для конвертации: ')

print(
    text.replace('>:)', '😈')
    .replace('>:(', '😠')
    .replace(':(', '🙁')
    .replace('XD', '😂')
    .replace(':)', '🙂')
)
