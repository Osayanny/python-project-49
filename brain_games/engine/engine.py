import prompt
from brain_games.engine.cli import welcome_user


_ROUNDS_COUNT = 3


def start_engine(game):
    name = welcome_user()
    print(f'{game.DESCRIPTION}')

    for _ in range(0, _ROUNDS_COUNT):
        question, game_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Answer: ')
        if user_answer == game_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(", end=' ')
            print(f"Correct answer was '{game_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
