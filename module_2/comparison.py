print('Я молодший брат НеЙмОвІрНоГо калькулятора - ймовірний порівняч 👋')
print('Потрібна допомога із числами? Введи два цілих числа і я підкажу яке більше, а яке менше')

first = int(input('Давай перше: '))
second = int(input('Давай друге: '))

if first < second:
    print('Перше менше другого!', first, '<', second)
elif first > second:
    print('Перше більше другого!', first, '>', second)
else:
    print('ОГО! А числа то, однакові!', first, '=', second)
    