import pathlib
import string


def read_file():
    with open(pathlib.Path(__file__).parent.joinpath("data.txt"), "r") as f:
        return f.readlines()


def extract_number(line):
    numbers = "".join([digit for digit in line if digit in string.digits])
    if len(numbers) > 2:
        numbers = numbers[:1] + numbers[-1:]
    if len(numbers) == 1:
        numbers *= 2
    return numbers


def part1():
    lines = read_file()
    line_numbers = []
    for line in lines:
        line_numbers.append(int(extract_number(line)))
    print(sum(line_numbers))


def part2():
    lines = read_file()
    line_numbers = []
    for line in lines:
        line = line.replace("zero", "z0o")
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        line_numbers.append(int(extract_number(line)))
    print(sum(line_numbers))


if __name__ == "__main__":
    part1()
    part2()
