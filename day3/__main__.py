import pathlib
import string


def read_file():
    with open(pathlib.Path(__file__).parent.joinpath("data.txt"), "r") as f:
        return f.readlines()


def parse_engine_schematics(data: list):
    data.insert(0, "." * len(data[1]))
    data.insert(len(data), "." * len(data[0]))
    schematics = []
    for line in data:
        if line.strip() == "":
            continue
        line = "." + line + "."
        schematics.append([char for char in line])
    w = len(schematics[0])
    h = len(schematics)
    return (schematics, h, w)


def get_number_with_borders(number_bound, schematics):
    left_upper_bound = number_bound[0]
    right_lower_bound = number_bound[1]
    temp = []
    for n, x in enumerate(range(left_upper_bound[0], right_lower_bound[0] + 1)):
        temp.append([])
        for y in range(left_upper_bound[1], right_lower_bound[1] + 1):
            t = schematics[x][y]
            temp[n].append(t)
    return temp


def get_number(number_bound, schematics):
    return int(
        "".join(
            schematics[number_bound[0][0] + 1][
                number_bound[0][1] + 1 : number_bound[1][1]
            ]
        )
    )


def is_adjacent_to_symbol(number_bound, schematics, h, w):
    left_upper_bound = number_bound[0]
    right_lower_bound = number_bound[1]
    for x in range(left_upper_bound[0], right_lower_bound[0] + 1):
        for y in range(left_upper_bound[1], right_lower_bound[1] + 1):
            char = schematics[x][y]

            if char in string.digits:
                continue
            if char == ".":
                continue
            return True
    return False


def part1():
    data = read_file()
    schematics, h, w = parse_engine_schematics(data)
    number_bounds_in_schematics = []
    for x in range(h):
        left_upper_bound = right_lower_bound = None
        for y in range(w):
            if schematics[x][y] in string.digits:
                if left_upper_bound is None:
                    left_upper_bound = (x - 1, y - 1)
                    right_lower_bound = (x + 1, y + 1)
                else:
                    right_lower_bound = (x + 1, y + 1)
            else:
                if left_upper_bound is not None:
                    assert right_lower_bound is not None
                if left_upper_bound is not None and right_lower_bound is not None:
                    assert left_upper_bound[0] + 2 == right_lower_bound[0]
                    number_bounds_in_schematics.append(
                        (left_upper_bound, right_lower_bound)
                    )
                    left_upper_bound = right_lower_bound = None
        if left_upper_bound is not None and right_lower_bound is not None:
            assert left_upper_bound[0] + 2 == right_lower_bound[0]
            number_bounds_in_schematics.append((left_upper_bound, right_lower_bound))
            left_upper_bound = right_lower_bound = None
    engine_parts = [
        (
            get_number(number_bound, schematics),
            get_number_with_borders(number_bound, schematics),
            is_adjacent_to_symbol(number_bound, schematics, h, w),
        )
        for number_bound in number_bounds_in_schematics
    ]
    engine_parts = [part for part in engine_parts if part[2]]
    print(sum([int(part[0]) for part in engine_parts]))


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
