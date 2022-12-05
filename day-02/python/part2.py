from itertools import product
import sys

A_NUM = 65
X_A_DIFF = 23
SHAPE_SCORE = dict(zip(("A", "B", "C"), range(1, 4)))


def translate_char(c):
    return chr(ord(c) - X_A_DIFF)


def char2idx(c):
    return ord(c) - A_NUM


def idx2char(i):
    return chr(i + A_NUM)


def roll(xs, shift):
    m = len(xs)
    return [xs[(i - shift) % m] for i in range(m)]


s = [3, 6, 0]
OUTCOME_SCORE = [s, roll(s, 1), roll(s, 2)]


def choose_move(opp_move, outcome):
    x = char2idx(opp_move)
    y = OUTCOME_SCORE[2 - x][char2idx(translate_char(outcome))] // 3
    return idx2char(y)


def main():
    sum_scores = 0
    for line in sys.stdin:
        line = line.rstrip()
        opp_move, outcome = line.split()
        my_move = choose_move(opp_move, outcome)
        outcome = OUTCOME_SCORE[char2idx(opp_move)][char2idx(my_move)]
        total_score = SHAPE_SCORE[my_move] + outcome
        sum_scores += total_score
    print(sum_scores)


if __name__ == "__main__":
    main()
