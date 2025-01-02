import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day17


def test_sets():
    return [
        {
            'number': 1,
            'input': {'register': {'A': None, 'B': None, 'C': 9}, 'program': [2, 6]},
            'expected1': {'register': {'A': None, 'B': 1, 'C': 9}, 'output': ''},
            'expected2': []
        },
        {
            'number': 2,
            'input': {'register': {'A': 10, 'B': None, 'C': None}, 'program': [5, 0, 5, 1, 5, 4]},
            'expected1': {'register': {'A': 10, 'B': None, 'C': None}, 'output': '0,1,2'},
            'expected2': []
        },
        {
            'number': 3,
            'input': {'register': {'A': 2024, 'B': None, 'C': None}, 'program': [0, 1, 5, 4, 3, 0]},
            'expected1': {'register': {'A': 0, 'B': None, 'C': None}, 'output': '4,2,5,6,7,7,7,7,3,1,0'},
            'expected2': []
        },
        {
            'number': 4,
            'input': {'register': {'A': None, 'B': 29, 'C': None}, 'program': [1, 7]},
            'expected1': {'register': {'A': None, 'B': 26, 'C': None}, 'output': ''},
            'expected2': []
        },
        {
            'number': 5,
            'input': {'register': {'A': None, 'B': 2024, 'C': 43690}, 'program': [4, 0]},
            'expected1': {'register': {'A': None, 'B': 44354, 'C': 43690}, 'output': ''},
            'expected2': []
        },
        {
            'number': 6,
            'input': {'register': {'A': 729, 'B': 0, 'C': 0}, 'program': [0, 1, 5, 4, 3, 0]},
            'expected1': {'register': {'A': 0, 'B': 0, 'C': 0}, 'output': '4,6,3,5,6,3,5,2,1,0'},
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day17.operate(test_data)
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
