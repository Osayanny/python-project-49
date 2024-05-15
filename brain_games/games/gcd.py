from brain_games.engine.special_funcs import generate_number


def find_gcd(nums_tuple):
    a = max(nums_tuple)
    b = min(nums_tuple)
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a


def gcd_logic():
    first_num = generate_number()
    second_num = generate_number()

    question = f'{first_num} {second_num}'

    nums_tuple = (first_num, second_num)
    answer = str(find_gcd(nums_tuple))

    return (question, answer)
