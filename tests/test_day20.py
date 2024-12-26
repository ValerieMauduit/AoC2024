import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day20
from AoC_tools.work_with_maps import AocMap


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                '###############', '#...#...#.....#', '#.#.#.#.#.###.#', '#S#...#.#.#...#', '#######.#.#.###',
                '#######.#.#...#', '#######.#.###.#', '###..E#...#...#', '###.#######.###', '#...###...#...#',
                '#.#####.#.###.#', '#.#...#.#.#...#', '#.#.#.#.#.#.###', '#...#...#...###', '###############'
            ],
            'expected1': [84, {2: 14, 4: 14, 6: 2, 8: 4, 10: 2, 12: 3, 20: 1, 36: 1, 38: 1, 40: 1, 64: 1}],
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    path = day20.original_track(AocMap(test_data))
    AocMap(test_data).display()
    length = len(path) - 1
    cheats = day20.get_all_cheats(path)
    if length != expected[0]:
        print("Your output (length) is:")
        print(length)
        raise Exception(f'This is not the solution, you should get {expected[0]}')
    if cheats != expected[1]:
        print("Your output (cheats) is:")
        print(cheats)
        raise Exception(f'This is not the solution, you should get {expected[1]}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day00.my_func(test_data)
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
