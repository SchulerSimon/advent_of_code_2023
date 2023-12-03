import pathlib


def read_file():
    with open(pathlib.Path(__file__).parent.joinpath("data.txt"), "r") as f:
        return f.readlines()


def parse_games(lines):
    game_dict = {}
    for game_number, game in enumerate(lines):
        game_number += 1
        game_dict[str(game_number)] = {}
        game = game.split(":")[1]
        rounds = game.split(";")
        for round_number, _round in enumerate(rounds):
            game_dict[str(game_number)][str(round_number)] = {}
            cubes = _round.split(",")
            red = green = blue = 0
            for cube in cubes:
                if "red" in cube:
                    red = int(cube.replace("red", "").strip())
                if "green" in cube:
                    green = int(cube.replace("green", "").strip())
                if "blue" in cube:
                    blue = int(cube.replace("blue", "").strip())
            game_dict[str(game_number)][str(round_number)].update({"red": int(red)})
            game_dict[str(game_number)][str(round_number)].update({"green": int(green)})
            game_dict[str(game_number)][str(round_number)].update({"blue": int(blue)})
    return game_dict


def is_game_possible(game: dict):
    for _, data in game.items():
        if data["red"] > 12:
            return False
        if data["green"] > 13:
            return False
        if data["blue"] > 14:
            return False
    return True


def get_minimum_set(game: dict):
    red = green = blue = 0
    for _, data in game.items():
        if data["red"] > red:
            red = data["red"]
        if data["green"] > green:
            green = data["green"]
        if data["blue"] > blue:
            blue = data["blue"]
    return (red, green, blue)


def part1():
    game_dict = parse_games(read_file())
    possible = []
    for game_number, game_data in game_dict.items():
        if is_game_possible(game_data):
            possible.append(int(game_number))
    print(sum(possible))


def part2():
    game_dict = parse_games(read_file())
    minimum_set = []
    for _, game_data in game_dict.items():
        minimum_set.append(get_minimum_set(game_data))
    powers = []
    for _set in minimum_set:
        powers.append(_set[0] * _set[1] * _set[2])
    print(sum(powers))


if __name__ == "__main__":
    part1()
    part2()
