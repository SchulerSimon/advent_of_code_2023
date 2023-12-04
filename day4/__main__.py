import pathlib
from typing import List, Tuple


def read_file():
    with open(pathlib.Path(__file__).parent.joinpath("data.txt"), "r") as f:
        return f.readlines()


def parse_numbers(data: List[str]):
    data = data.split(" ")
    temp = []
    for number in data:
        number.strip()
        if number == "":
            continue
        else:
            temp.append(int(number))
    return temp


def parse_cards(data: List[str]):
    cards = []
    for line in data:
        line = line.split(":")[1]
        line = line.split("|")
        cards.append((parse_numbers(line[0]), parse_numbers(line[1])))
    return cards


def count_matches(card: Tuple[List[str]]):
    winning_numbers = card[0]
    my_numbers = card[1]
    matches = 0
    for number in my_numbers:
        if number in winning_numbers:
            matches += 1
    return matches


def matches_to_score(matches: int):
    if matches == 0:
        return 0
    else:
        return 2 ** (matches - 1)


def part1():
    data = read_file()
    cards = parse_cards(data)
    matches = [count_matches(card) for card in cards]
    scores = [matches_to_score(match) for match in matches]
    print(sum(scores))


def part2():
    # no more time :/
    pass


if __name__ == "__main__":
    part1()
    part2()
