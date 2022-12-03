import sys


def main():
    a = 0
    amax = 0
    for l in sys.stdin:
        l = l.rstrip()
        if l == '':
            amax = max(amax, a)
            a = 0
        else:
            a += int(l)
    print(amax)


if __name__ == "__main__":
    main()

