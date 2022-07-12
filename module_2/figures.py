# Square
SIZE = 10
for x in range(SIZE):
    for y in range(SIZE):
        place(x, 0, y)

# Cube
SIZE = 5
for x in range(SIZE):
    for y in range(SIZE):
        for z in range(SIZE):
            if sum((x in (0, (SIZE - 1)), y in (0, (SIZE - 1)), z in (0, (SIZE - 1)),)) >= 2:
                place(x, y, z)

# Circle
RADIUS = 10
RAD2 = RADIUS ** 2
for x in range(-RADIUS, RADIUS + 1):
    for y in range(-RADIUS, RADIUS + 1):
        if RAD2 * 0.9 <= x ** 2 + y ** 2 <= RAD2 * 1.1:
            place(x, y, 0)
