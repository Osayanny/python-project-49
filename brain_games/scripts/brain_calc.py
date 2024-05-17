#!usr/bin/env python3


from brain_games.engine.engine import engine
from brain_games.games.calc import calc_logic


def main():
    description = 'What is the result of the expression?'
    engine(description, calc_logic)


if __name__ == '__main__':
    main()
