#!usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.even import generate_number, is_even


def main():
    print('Welcome to the Brain Games')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    correct = 0
    while correct != 3:
        number = generate_number()
        print(f'Question: {number}')
        answer = input('Answer: ')
        correct_answer = is_even(number)
        if correct_answer == answer:
            print('Correct!')
            correct += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratultions, {name}!')


if __name__ == '__main__':
    main()
