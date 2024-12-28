import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.work_with_maps import AocMap
from all_days import day16


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                '###############', '#.......#....E#', '#.#.###.#.###.#', '#.....#.#...#.#', '#.###.#####.#.#',
                '#.#.#.......#.#', '#.#.#####.###.#', '#...........#.#', '###.#.#####.#.#', '#...#.....#.#.#',
                '#.#.#.###.#.#.#', '#.....#...#.#.#', '#.###.#.#.#.#.#', '#S..#.....#...#', '###############'
            ],
            'expected1': 7036,
            'expected2': 45
        },
        {
            'number': 2,
            'input': [
                '#################', '#...#...#...#..E#', '#.#.#.#.#.#.#.#.#', '#.#.#.#...#...#.#', '#.#.#.#.###.#.#.#',
                '#...#.#.#.....#.#', '#.#.#.#.#.#####.#', '#.#...#.#.#.....#', '#.#.#####.#.###.#', '#.#.#.......#...#',
                '#.#.###.#####.###', '#.#.#...#.....#.#', '#.#.#.#####.###.#', '#.#.#.........#.#', '#.#.#.#########.#',
                '#S#.............#', '#################'
            ],
            'expected1': 11048,
            'expected2': 64
        }
    ]


def test_first_star(test_data, expected):
    solution = day16.reinder_score(AocMap(test_data))
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day16.get_spots(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def main():
    test_case = int(input('Which star to test? '))
    for test in test_sets():
        print(f"=== Test #{test['number']} ===")
        if test_case == 1:
            test_first_star(test['input'], test['expected1'])
        elif test_case == 2:
            test_second_star(test['input'], test['expected2'])
        else:
            print("Error, the star must be 1 or 2.")


if __name__ == '__main__':
    main()
