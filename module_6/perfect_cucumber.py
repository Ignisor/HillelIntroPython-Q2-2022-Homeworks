print(
    'Привіт! Мені дуже потрібен Cucumber прямо зараз, введи мені Cucumber будь ласка!\n'
    'Але будь уважним, неймовірно важливо щоб Cucumber був гарний та без помилок!'
)


def validations(cucumber):
    assert (
        ' ' not in cucumber
    ), 'Щось я не памʼятаю щоб у Cucumber були пробіли. Буду вважати що це випадковість...'

    assert 'cucumber' in cucumber.lower(), 'Тут взагалі нема Cucumber!'

    assert cucumber.startswith('C'), (
        'О ні! Ну хто ж так робить!'
        ' Твій Cucumber починається з маленької літери, виправляй швиденько'
    )

    assert cucumber[1:].islower(), 'Що за кривий Cucumber? А ну вирівнюй!'

    assert cucumber.lower() == 'cucumber', 'Тут щось зайве - прибери'


while True:
    cucumber_input = input('Давай, я в тебе вірю: ')

    try:
        validations(cucumber_input)
    except AssertionError as error:
        print(error, '😡')
    else:
        print('Відмінно! Дуже дякую! Ти, буквально, врятував всесвіт 😊')
        break
