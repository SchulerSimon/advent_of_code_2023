import pathlib
from typing import List

test = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def read_file():
    # return test.split("\n")
    with open(pathlib.Path(__file__).parent.joinpath("data.txt"), "r") as f:
        return f.readlines()


def get_seeds(data: List[str]):
    for line in data:
        if line.startswith("seeds:"):
            return [int(seed) for seed in line.replace("seeds:", "").strip().split(" ")]


def get_seeds_from_range(data: List[str]):
    seed_pairs = get_seeds(data)
    seed_pairs = [(seed, r) for seed, r in zip(seed_pairs[::2], seed_pairs[1::2])]
    for seed, r in seed_pairs:
        for s in range(seed, seed + r):
            yield s

def get_map(source, dest, data: List[str]):
    _map = []
    map_started = False
    for line in data:
        if line.startswith(source + "-to-" + dest):
            map_started = True
            continue
        if map_started:
            if line.strip() == "":
                break
            else:
                _map.append([int(n) for n in line.split(" ")])
    return _map


def use_map(input, m):
    for number in input:
        number_mapped = False
        for dest, source, _range in m:
            if number >= source and number <= source + _range:
                yield dest + (number - source)
                number_mapped = True
                break
        if not number_mapped:
            yield number


def part1():
    data = read_file()
    seeds = get_seeds(data)
    l = [
        "seed",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]
    r = seeds
    for source, dest in zip(l, l[1:]):
        m = get_map(source, dest, data)
        r = [m for m in use_map(r, m)]
    print(min(r))


def part2():
    data = read_file()
    seeds = get_seeds_from_range(data)
    l = [
        "seed",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]
    # originally use_map and get_seeds_from_range just returned lists, 
    # but with the acutal data, my RAM was full within seconds. 
    # So I rewrote them to be generators.
    # It still takes my i7 about 5 minutes to get a result for part2
    # I am sure this could be optimized qute a lot. 
    # But memory dosent get out of control anymore :D 
    # So I guess that solution is "good enough"
    _min = 2**100
    for seed in seeds:
        r = seed
        for source, dest in zip(l, l[1:]):
            m = get_map(source, dest, data)
            r = next(use_map([r], m))
            if r < _min:
                _min = r
    print(_min)
            


if __name__ == "__main__":
    part1()
    part2()
