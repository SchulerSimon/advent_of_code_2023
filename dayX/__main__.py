import pathlib


def read_file():
    with open(pathlib.Path(__file__).parent.joinpath("data.txt"), "r") as f:
        return f.readlines()


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
