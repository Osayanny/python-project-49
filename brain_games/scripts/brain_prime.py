#!usr/bin env python3
from brain_games.games import prime
from brain_games.engine.engine import start_engine


def main():
    start_engine(prime)


if __name__ == '__main__':
    main()
