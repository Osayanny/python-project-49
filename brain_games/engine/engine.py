from brain_games.engine.cli import welcome_user


def is_correct(user_answer, game_answer):
    if game_answer == user_answer:
        return True
    return False


def engine(discription, game_logic):
    name = welcome_user()
    print(f'{discription}')
    correct = 0
    while correct != 3:
        question, game_answer = game_logic()
        print(f'Question: {question}')
        user_answer = input('Answer: ')
        if is_correct(user_answer, game_answer):
            print('Correct!')
            correct += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(", end='')
            print(f"Correct answer was '{game_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
