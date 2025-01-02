import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day12


def test_sets():
    return [
        {
            'number': 1,
            'input': ['AAAA', 'BBCD', 'BBCC', 'EEEC'],
            'expected1': 140,
            'expected2': 80
        },
        {
            'number': 2,
            'input': ['OOOOO', 'OXOXO', 'OOOOO', 'OXOXO', 'OOOOO'],
            'expected1': 772,
            'expected2': 436
        },
        {
            'number': 3,
            'input': [
                'RRRRIICCFF', 'RRRRIICCCF', 'VVRRRCCFFF', 'VVRCCCJFFF', 'VVVVCJJCFE', 'VVIVCCJJEE', 'VVIIICJJEE',
                'MIIIIIJJEE', 'MIIISIJEEE', 'MMMISSJEEE'
            ],
            'expected1': 1930,
            'expected2': 1206
        },
        {
            'number': 4,
            'input': ['EEEEE', 'EXXXX', 'EEEEE', 'EXXXX', 'EEEEE'],
            'expected1': 692,
            'expected2': 236
        },
        {
            'number': 5,
            'input': ['AAAAAA', 'AAABBA', 'AAABBA', 'ABBAAA', 'ABBAAA', 'AAAAAA'],
            'expected1': 1184,
            'expected2': 368
        },

    ]


def test_first_star(test_data, expected):
    solution = day12.fencing_price(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day12.fencing_price(test_data, with_discount=True)
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
