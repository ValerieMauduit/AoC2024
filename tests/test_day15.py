import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from all_days import day15


def test_sets():
    return [
        {
            'number': 1,
            'input': [
                ['########', '#..O.O.#', '##@.O..#', '#...O..#', '#.#.O..#', '#...O..#', '#......#', '########'],
                ['WNNEEESSWSEESWW']
            ],
            'expected1': 2028,
            'expected2': 1751
        },
        {
            'number': 2,
            'input': [
                [
                    '##########', '#..O..O.O#', '#......O.#', '#.OO..O.O#', '#..O@..O.#', '#O#..O...#', '#O..O..O.#',
                    '#.OO.O.OO#', '#....O...#', '##########'
                ],
                [
                    'WSSENWSNESENSSNSESWESNSWSWNSSWWWNEWWEWEESWSSSWENSNENWWWEWWSWWWSNSSNSEN',
                    'SSSWWNENSNNEWWEEEWENWWEWNSSNNWESSSWEEWNNSENESSWESWWWWSWNSENWNNEEENWSWS',
                    'EWESSESNSNWEEWEEEEWNNESSESWNNNEESNSNWNNESNNESNWNSESWEESNSNWSESNNWNNSSW',
                    'WWSWNEENNNNEEESNWESSSNEWSWWWENNNSSNWSSSENESWNNNNSWENESSSSEWEESNWWNNNNN',
                    'NEWNEWEEEWENNWWNNSEEEWNWSENWSSEESEEENSEWENSEWWWWSEESWSWSESSSENWEWWENEW',
                    'NEEWENSWEWNSSSWNNWEWSWWWWWEWNSWWWEWWWNNWSWNNNEWNEENWSNEWWWNEENSWSNSWSN',
                    'ENEENSESSENWWNSWEEWWEWWSWWSEWESWNSSWWWENNSNENNEEEWWNSEESNSEWNNEENWESSN',
                    'WEWNNENNNWEWSSSSSNSWSWWENSWSESWWNEWWEWWEWWWNNWWWNWWEEWWEWNNNENNWENESWE',
                    'NNESSWNSNSWSSENWEWSWNSENNNEEENNSSSNESSSWEEENWNEEEEENWWNSENSSSWENWEWWSE',
                    'SNNEEEWWNNWEENSNWSNSSWESNWWENWNSNSEWNWWWEWWNWSEWSWESSEESEWSNWSSWESNWWN'
                ]
            ],
            'expected1': 10092,
            'expected2': 9021
        },
    ]


def test_first_star(test_data, expected):
    solution = day15.check_sum(test_data)
    if solution != expected:
        print("Your output is:")
        print(solution)
        raise Exception(f'This is not the solution, you should get {expected}')
    print('--- Test OK')


def test_second_star(test_data, expected):
    solution = day15.second_warehouse_checksum(test_data)
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
