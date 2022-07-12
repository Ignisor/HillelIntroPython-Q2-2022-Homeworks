import argparse
from pathlib import Path
import random

import requests

URL = 'http://placekitten.com'
SIZE_RANGE = (100, 1000)


def get_cat_picture(width, height, filename, gray=False):
    url = f'{URL}{"/g" if gray else ""}/{width}/{height}'
    response = requests.get(url)

    with open(filename, 'wb') as catfile:
        for chunk in response:
            catfile.write(chunk)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Створювач кицьок :3')
    parser.add_argument('amount', type=int, help='Кількість картинок з кицями')
    parser.add_argument(
        'out_dir', nargs='?', default='.', help='Директорія для збереження картинок',
    )
    parser.add_argument(
        '--gray',
        action='store_true',
        default=False,
        help='Створювати чорно-білих кицьок',
    )

    args = parser.parse_args()

    print('Вітаю у створювачі кицьок :3')
    print(
        f'Зараз створю тобі {args.amount} картинок '
        f'з {"чорно-білими " if args.gray else ""}'
        f'кицями у директорії {args.out_dir}'
    )
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1, args.amount + 1):
        width = random.randint(*SIZE_RANGE)
        height = random.randint(*SIZE_RANGE)
        filename = out_dir / f'cat_{i}.jpg'

        print(f'Створюю котика номер {i} у розмірі {width}x{height}')
        get_cat_picture(width, height, filename, gray=args.gray)

    print('Створення кицьок завершено! Насолоджуйтеся :3')
