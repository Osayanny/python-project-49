import random
from brain_games.engine.special_funcs import generate_number


def make_progression():
    start = generate_number()
    step = generate_number((1, 10))
    stop = start + step * 10
    return [str(i) for i in range(start, stop, step)]


def progression_logic():
    progression = make_progression()
    answer = random.choice(progression)
    answer_index = progression.index(answer)
    progression[answer_index] = '..'
    question = ' '.join(progression)
    return (question, answer)
