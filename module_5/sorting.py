import random

numbers = [random.randint(0, 100) for _ in range(10)]
print('Initial list:', numbers)


def sort_list(numbers):
    sorted_numbers = numbers[::]
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sorted_numbers[i] > sorted_numbers[j]:
                sorted_numbers[i], sorted_numbers[j] = (
                    sorted_numbers[j],
                    sorted_numbers[i],
                )

    return sorted_numbers


print('Sorted list:', sort_list(numbers))
