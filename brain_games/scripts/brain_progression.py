#!usr/bin/env python3
from brain_games.engine.engine import engine
from brain_games.games.progression import progression_logic


def main():
    description = 'What number is missing in the progression?'
    engine(discription, progression_logic)


if __name__ == '__main__':
    main()
