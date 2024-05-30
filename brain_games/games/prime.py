import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_STOP = 100
_START = 1


def is_prime(num):

    for div in range(2, num):
        if num % div == 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(_START, _STOP)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
