import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day14


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                'p=0,4 v=3,-3', 'p=6,3 v=-1,-3', 'p=10,3 v=-1,2', 'p=2,0 v=2,-1', 'p=0,0 v=1,3', 'p=3,0 v=-2,-2',
                'p=7,6 v=-1,-3', 'p=3,0 v=-1,-2', 'p=9,3 v=2,3', 'p=7,3 v=-1,2', 'p=2,4 v=2,-3', 'p=9,5 v=-3,-3'
            ],
            'expected1': 12,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day14.safety_result(test_data, steps=100, width=11, height=7)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
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
