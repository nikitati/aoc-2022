from itertools import islice
import sys

OFFSET_LOWER = 96
OFFSET_UPPER = 38
LOWER_BOUNDS = (ord('a'), ord('z'))
UPPER_BOUNDS = (ord('A'), ord('Z'))


def get_priority(char):
    value = ord(char)
    if value >= LOWER_BOUNDS[0] and value <= LOWER_BOUNDS[1]:
        return value - OFFSET_LOWER
    elif value >= UPPER_BOUNDS[0] and value <= UPPER_BOUNDS[1]:
        return value - OFFSET_UPPER


def main():
    sum_priorities = 0
    while (sacks := list(islice(map(str.rstrip, sys.stdin), 3))):
        common = set.intersection(*map(set, sacks))
        priorities = sum(map(get_priority, common))
        sum_priorities += priorities
    print(sum_priorities)


if __name__ == "__main__":
    main()
