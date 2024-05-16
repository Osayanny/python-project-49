import random

# Uneversal functions


def generate_number(gen_range=(1, 100)):
    first_bord, second_bord = gen_range
    number = random.randint(first_bord, second_bord)
    return number
