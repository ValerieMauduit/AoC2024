import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day22


def test_sets():
    return [
        {
            'number': 1,
            'input': {'numbers': [123 for _ in range(1, 11)], 'rounds': [x for x in range(1, 11)]},
            'expected1': [15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254],
            'expected2': 60
        },
        {
            'number': 2,
            'input': {'numbers': [1, 10, 100, 2024], 'rounds': [2000 for _ in range(4)]},
            'expected1': [8685429, 4700978, 15273692, 8667524],
            'expected2': 23
        },
    ]


def test_first_star(test_data, expected):
    solution = [day22.get_secret(number, steps) for number, steps in zip(test_data['numbers'], test_data['rounds'])]
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day22.find_best_deal(test_data['numbers'], test_data['rounds'][-1])
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
