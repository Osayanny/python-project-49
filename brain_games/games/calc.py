import random


DESCRIPTION = 'What is the result of the expression?'
_STOP = 100
_START = 1


def get_question_and_answer():
    operators = ['+', '-', '*']
    operand_1 = random.randint(_START, _STOP)
    operand_2 = random.randint(_START, _STOP)
    operator = random.choice(operators)

    question = f'{operand_1} {operator} {operand_2}'

    if operator == '+':
        answer = operand_1 + operand_2
    elif operator == '-':
        answer = operand_1 - operand_2
    elif operator == '*':
        answer = operand_1 * operand_2

    return question, str(answer)
