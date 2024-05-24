import random


DESCRIPTION = 'What is the result of the expression?'
_TOP_BOUND = 100
_BOTTOM_BOUND = 1


def get_question_and_answer():
    operators = ['+', '-', '*']
    operand_1 = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    operand_2 = random.randint(_BOTTOM_BOUND, _TOP_BOUND)
    operator = random.choice(operators)
    question = f'{operand_1} {operator} {operand_2}'
    if operator == '+':
        answer = operand_1 + operand_2
    elif operator == '-':
        answer = operand_1 - operand_2
    elif operator == '*':
        answer = operand_1 * operand_2
    return question, answer
