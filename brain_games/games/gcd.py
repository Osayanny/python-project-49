import random
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
_TOP_BOUND = 100
_BOTTOM_BOUND = 1


def get_logic():
    first_num = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    second_num = random.randint(_BOTTOM_BOUND, _TOP_BOUND)

    question = f'{first_num} {second_num}'

    answer = gcd(first_num, second_num)

    return question, answer
