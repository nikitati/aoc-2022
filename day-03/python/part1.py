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
    for line in map(str.rstrip, sys.stdin):
        middle = len(line) // 2
        l, r = line[:middle], line[middle:]
        common = set(l) & set(r)
        priorities = sum(map(get_priority, common))
        sum_priorities += priorities
    print(sum_priorities)


if __name__ == "__main__":
    main()
