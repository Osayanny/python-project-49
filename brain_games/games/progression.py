import random


DESCRIPTION = 'What number is missing in the progression?'
_STOP = 100
_START = 1
_STEP_START = 1
_STEP_STOP = 10
_ELEMENTS_START = 3
_ELEMENTS_STOP = 10


def make_progression():
    start = random.randint(_START, _STOP)
    step = random.randint(_STEP_START, _STEP_STOP)
    elements_count = random.randint(_ELEMENTS_START, _ELEMENTS_STOP)
    stop = start + step * elements_count
    return [str(i) for i in range(start, stop, step)]


def get_question_and_answer():
    progression = make_progression()
    answer = random.choice(progression)
    answer_index = progression.index(answer)
    progression[answer_index] = '..'
    question = ' '.join(progression)
    return question, str(answer)
