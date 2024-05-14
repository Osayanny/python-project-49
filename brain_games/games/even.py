from brain_games.engine.special_funcs import generate_number


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def even_logic():
    question = generate_number()
    answer = is_even(question)
    return (question, answer)
