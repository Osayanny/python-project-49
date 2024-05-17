#!usr/bin env python3
from brain_games.engine.engine import engine
from brain_games.games.prime import prime_logic


def main():
    desc_part_one = 'Answer "yes" if given number is prime.'
    desc_part_two = 'Otherwise answer "no".'
    description = f'{desc_part_one} {desc_part_two}'
    engine(description, prime_logic)


if __name__ == '__main__':
    main()
