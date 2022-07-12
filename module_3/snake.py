import time
import random


print('Зараз буде змійка :3')
time.sleep(1)

width = 20
position = width // 2

while True:
    try:
        time.sleep(0.1)
        position += random.choice([-1, 0, 1])
        position = min(max(0, position), width - 1)

        row = ' ' * (position - 1) + '*' + ' ' * (width - position)
        print(row)
    except KeyboardInterrupt:
        row = ' ' * (position - 4) + '0_0' + ' ' * (width - position)
        print(row)
        break
