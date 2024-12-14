import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day13


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                ['Button A: X+94, Y+34', 'Button B: X+22, Y+67', 'Prize: X=8400, Y=5400'],
                ['Button A: X+26, Y+66', 'Button B: X+67, Y+21', 'Prize: X=12748, Y=12176'],
                ['Button A: X+17, Y+86', 'Button B: X+84, Y+37', 'Prize: X=7870, Y=6450'],
                ['Button A: X+69, Y+23', 'Button B: X+27, Y+71', 'Prize: X=18641, Y=10279']
            ],
            'expected1': 480,
            'expected2': 875318608908
        },
    ]


def test_first_star(test_data, expected):
    solution = day13.play_all_arcades(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day13.play_all_arcades(test_data, 10000000000000)
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
