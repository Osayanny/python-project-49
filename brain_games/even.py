import random


def generate_number():
    return random.randint(1, 100)


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'
