import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
_TOP_BOUND = 100
_BOTTOM_BOUND = 1


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def get_question_and_answer():
    question = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
