from brain_games.engine.cli import welcome_user


def start_engine(module):
    name = welcome_user()
    print(f'{module.DESCRIPTION}')
    rounds_count = 3
    correct = 0
    while correct != rounds_count:
        question, game_answer = module.get_logic()
        print(f'Question: {question}')
        user_answer = input('Answer: ')
        if user_answer == str(game_answer):
            print('Correct!')
            correct += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(", end=' ')
            print(f"Correct answer was '{game_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
