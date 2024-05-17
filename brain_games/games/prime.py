from brain_games.engine.special_funcs import generate_number


def is_prime(num):
    divisiors = [_ for _ in range(1, num+1)]
    divisiors_count = 0

    for i in divisiors:
        if num % i == 0:
            divisiors_count += 1

        if divisiors_count > 2:
            return 'no'
    return 'yes'


def prime_logic():
    question = generate_number()
    answer = is_prime(question)
    return question, answer
