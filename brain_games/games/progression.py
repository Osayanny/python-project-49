import random


DESCRIPTION = 'What number is missing in the progression?'
_TOP_BOUND = 100
_BOTTOM_BOUND = 1
_TOP_STEP_BOUND = 10
_EL_IN_PROGRESS = 10


def make_progression():
    start = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    step = random.randint(_BOTTOM_BOUND, _TOP_STEP_BOUND)
    stop = start + step * _EL_IN_PROGRESS
    return [str(i) for i in range(start, stop, step)]


def get_logic():
    progression = make_progression()
    answer = random.choice(progression)
    answer_index = progression.index(answer)
    progression[answer_index] = '..'
    question = ' '.join(progression)
    return question, answer
