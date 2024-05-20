import random


DESCRIPTION = 'What is the result of the expression?'
_TOP_BOUND = 100
_BOTTOM_BOUND = 1


def get_logic():
    operators_list = ['+', '-', '*']
    oper_1 = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    oper_2 = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    operator = random.choice(operators_list)
    question = f'{oper_1} {operator} {oper_2}'
    if operator == '+':
        answer = oper_1 + oper_2
    elif operator == '-':
        answer = oper_1 - oper_2
    elif operator == '*':
        answer = oper_1 * oper_2
    return question, answer
