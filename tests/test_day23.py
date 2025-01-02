import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day23


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                ['kh', 'tc'], ['qp', 'kh'], ['de', 'cg'], ['ka', 'co'], ['yn', 'aq'], ['qp', 'ub'], ['cg', 'tb'],
                ['vc', 'aq'], ['tb', 'ka'], ['wh', 'tc'], ['yn', 'cg'], ['kh', 'ub'], ['ta', 'co'], ['de', 'co'],
                ['tc', 'td'], ['tb', 'wq'], ['wh', 'td'], ['ta', 'ka'], ['td', 'qp'], ['aq', 'cg'], ['wq', 'ub'],
                ['ub', 'vc'], ['de', 'ta'], ['wq', 'aq'], ['wq', 'vc'], ['wh', 'yn'], ['ka', 'de'], ['kh', 'ta'],
                ['co', 'tc'], ['wh', 'qp'], ['tb', 'vc'], ['td', 'yn']
            ],
            'expected1': 7,
            'expected2': 'co,de,ka,ta'
        },
    ]


def test_first_star(test_data, expected):
    solution = day23.count_lans(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day23.find_max_full_network(test_data)
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
