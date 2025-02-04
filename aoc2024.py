#! /usr/bin/env python
import argparse

from all_days import (
    day01, day02, day03, day04, day05, day06, day07, day08, day09, day10, day11, day12,
    day13, day14, day15, day16, day17, day18, day19, day20, day21, day22, day23, day24,
    day25
)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2024")
    parser.add_argument("--day", type=int, help="Puzzle day")
    parser.add_argument("--star", type=int, help="Puzzle star")
    parser.add_argument('--dir', type=str, help='Input data directory')
    args = parser.parse_args()

    if args.day == 1:
        day01.run(args.dir, args.star)
    elif args.day == 2:
        day02.run(args.dir, args.star)
    elif args.day == 3:
        day03.run(args.dir, args.star)
    elif args.day == 4:
        day04.run(args.dir, args.star)
    elif args.day == 5:
        day05.run(args.dir, args.star)
    elif args.day == 6:
        day06.run(args.dir, args.star)
    elif args.day == 7:
        day07.run(args.dir, args.star)
    elif args.day == 8:
        day08.run(args.dir, args.star)
    elif args.day == 9:
        day09.run(args.dir, args.star)
    elif args.day == 10:
        day10.run(args.dir, args.star)
    elif args.day == 11:
        day11.run(args.dir, args.star)
    elif args.day == 12:
        day12.run(args.dir, args.star)
    elif args.day == 13:
        day13.run(args.dir, args.star)
    elif args.day == 14:
        day14.run(args.dir, args.star)
    elif args.day == 15:
        day15.run(args.dir, args.star)
    elif args.day == 16:
        day16.run(args.dir, args.star)
    elif args.day == 17:
        day17.run(args.dir, args.star)
    elif args.day == 18:
        day18.run(args.dir, args.star)
    elif args.day == 19:
        day19.run(args.dir, args.star)
    elif args.day == 20:
        day20.run(args.dir, args.star)
    elif args.day == 21:
        day21.run(args.dir, args.star)
    elif args.day == 22:
        day22.run(args.dir, args.star)
    elif args.day == 23:
        day23.run(args.dir, args.star)
    elif args.day == 24:
        day24.run(args.dir, args.star)
    elif args.day == 25:
        day25.run(args.dir, args.star)
    else:
        raise Exception("Day isn't already coded")


if __name__ == "__main__":
    main()
