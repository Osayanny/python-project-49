import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
_STOP = 100
_START = 1


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_question_and_answer():
    question = random.randint(_START, _STOP)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
