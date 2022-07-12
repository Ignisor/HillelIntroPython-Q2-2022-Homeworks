print('Щас найдем огурец 🥒')
text = input('Введите фразу со словом "cucumber": ')

cucumber_i = text.find('cucumber')
if cucumber_i >= 0:
    print(text[cucumber_i:])
else:
    print('"cucumber" не найден... Ну блин, я ж просил 😢')
