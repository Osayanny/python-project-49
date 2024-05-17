#!usr/bin env python3
from brain_games.engine.engine import engine
from brain_games.games.prime import prime_logic


def main():
    discription = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(discription, prime_logic)


if __name__ == '__main__':
    main()
