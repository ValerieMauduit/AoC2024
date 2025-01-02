import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day07


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                [190, [10, 19]], [3267, [81, 40, 27]], [83, [17, 5]], [156, [15, 6]], [7290, [6, 8, 6, 15]],
                [161011, [16, 10, 13]], [192, [17, 8, 14]], [21037, [9, 7, 18, 13]], [292, [11, 6, 16, 20]]
            ],
            'expected1': 3749,
            'expected2': 11387
        },
    ]


def test_first_star(test_data, expected):
    solution = day07.calibration_result(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day07.calibration_result(test_data, with_concatenation=True)
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
