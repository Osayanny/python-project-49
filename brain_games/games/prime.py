import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_TOP_BOUND = 100
_BOTTOM_BOUND = 1


def is_prime(num):
    if num < 2:
        return False

    divisiors_count = 0
    for div in range(1, num + 1):
        if num % div == 0:
            divisiors_count += 1

        if divisiors_count > 2:
            return False
    return True


def get_question_and_answer():
    question = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
