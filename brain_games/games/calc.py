import random
from brain_games.engine.special_funcs import generate_number


def calc_logic():
    operators_list = ['+', '-', '*']
    oper_1 = generate_number()
    oper_2 = generate_number()
    operator = random.choice(operators_list)
    question = f'{oper_1}{operator}{oper_2}'
    answer = str(eval('oper_1' + operator + 'oper_2'))
    return (question, answer)
