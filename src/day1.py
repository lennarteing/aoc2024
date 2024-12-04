import collections
import os


def main():

    with open(os.path.abspath('/home/lennarteing/.aoc_puzzles/2024/day-1.txt'), 'r') as left:
        lines = [l.strip().split('   ') for l in left.readlines()]

    left, right = zip(*lines)
    left = list(sorted(map(int, left)))
    right = list(sorted(map(int, right)))
    dist = list(map(lambda x: abs(x[1] - x[0]), zip(left, right)))
    total_dist = sum(dist)
    print(f'Day 1, Part 1: {total_sim}')

    counts = collections.Counter(right)
    sim = map(lambda l: counts[l] * l, left)
    total_sim = sum(sim)
    print(f'Day 1, Part 2: {total_sim}')


if __name__ == '__main__':
    main()
