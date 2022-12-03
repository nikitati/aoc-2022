import sys
import heapq


def main():
    a = 0
    heap = list()
    for l in sys.stdin:
        l = l.rstrip()
        if l == '':
            if len(heap) >= 3:
                heapq.heappushpop(heap, a)
            else:
                heapq.heappush(heap, a)
            a = 0
        else:
            a += int(l)
    print(sum(heap))


if __name__ == "__main__":
    main()

