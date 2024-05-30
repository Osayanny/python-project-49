import random
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
_STOP = 100
_START = 1


def get_question_and_answer():
    first_num = random.randint(_START, _STOP)
    second_num = random.randint(_START, _STOP)

    question = f'{first_num} {second_num}'

    answer = gcd(first_num, second_num)

    return question, str(answer)
