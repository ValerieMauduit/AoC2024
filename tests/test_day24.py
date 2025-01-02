import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day24


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                ['x00: 1', 'x01: 1', 'x02: 1', 'y00: 0', 'y01: 1', 'y02: 0'],
                ['x00 AND y00 -> z00', 'x01 XOR y01 -> z01', 'x02 OR y02 -> z02']
            ],
            'expected1': 4,
            'expected2': []
        },
        {
            'number': 2,
            'input': [
                ['x00: 1', 'x01: 0', 'x02: 1', 'x03: 1', 'x04: 0', 'y00: 1', 'y01: 1', 'y02: 1', 'y03: 1', 'y04: 1'],
                [
                    'ntg XOR fgs -> mjb', 'y02 OR x01 -> tnw', 'kwq OR kpj -> z05', 'x00 OR x03 -> fst',
                    'tgd XOR rvg -> z01', 'vdt OR tnw -> bfw', 'bfw AND frj -> z10', 'ffh OR nrd -> bqk',
                    'y00 AND y03 -> djm', 'y03 OR y00 -> psh', 'bqk OR frj -> z08', 'tnw OR fst -> frj',
                    'gnj AND tgd -> z11', 'bfw XOR mjb -> z00', 'x03 OR x00 -> vdt', 'gnj AND wpb -> z02',
                    'x04 AND y00 -> kjc', 'djm OR pbm -> qhw', 'nrd AND vdt -> hwm', 'kjc AND fst -> rvg',
                    'y04 OR y02 -> fgs', 'y01 AND x02 -> pbm', 'ntg OR kjc -> kwq', 'psh XOR fgs -> tgd',
                    'qhw XOR tgd -> z09', 'pbm OR djm -> kpj', 'x03 XOR y03 -> ffh', 'x00 XOR y04 -> ntg',
                    'bfw OR bqk -> z06', 'nrd XOR fgs -> wpb', 'frj XOR qhw -> z04', 'bqk OR frj -> z07',
                    'y03 OR x01 -> nrd', 'hwm AND bqk -> z03', 'tgd XOR rvg -> z12', 'tnw OR pbm -> gnj'
                ]
            ],
            'expected1': 2024,
            'expected2': []
        },
    ]


def test_first_star(test_data, expected):
    solution = day24.calculate(test_data)
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
