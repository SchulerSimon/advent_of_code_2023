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


def calc_number_of_cards(all_matches, start, stop):
    result = 1
    for card_index, match in enumerate(all_matches[start - 1 : stop - 1]):
        if match == 0:
            result += 1
        else:
            _from = start + 1 + card_index
            _to = _from + match
            result += calc_number_of_cards(all_matches, start=_from, stop=_to)
    return result


def part1():
    data = read_file()
    cards = parse_cards(data)
    matches = [count_matches(card) for card in cards]
    scores = [matches_to_score(match) for match in matches]
    print(sum(scores))


def part2():
    data = read_file()
    cards = parse_cards(data)
    matches = [count_matches(card) for card in cards]
    result = calc_number_of_cards(matches, start=1, stop=len(matches))
    print(result)


if __name__ == "__main__":
    part1()
    part2()
