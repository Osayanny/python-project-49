#!usr/bin/env python3
from brain_games.engine.engine import engine
from brain_games.games.even import even_logic


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(discription, even_logic)


if __name__ == '__main__':
    main()
