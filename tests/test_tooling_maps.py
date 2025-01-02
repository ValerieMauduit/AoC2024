import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import work_with_maps


@pytest.fixture
def mocked_map():
    return work_with_maps.AocMap(['....#.', '...##.', '#.....'], [5, 1])


@pytest.fixture
def test_coordinates():
    return [[1, 5], [3, 2]]


def test_init(mocked_map):
    assert mocked_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    assert mocked_map.width == 6
    assert mocked_map.height == 3
    assert mocked_map.x == 5
    assert mocked_map.y == 1


def test_empty_from_size():
    my_map = work_with_maps.AocMap.empty_from_size(3, 4)
    assert my_map.map == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    assert my_map.width == 3
    assert my_map.height == 4


def test_from_coord(test_coordinates):
    without_origin = work_with_maps.AocMap.from_coord(test_coordinates)
    assert without_origin.origin == [1, 2]
    assert without_origin.map == [['.', '.', '#'], ['.', '.', '.'], ['.', '.', '.'], ['#', '.', '.']]
    with_origin = work_with_maps.AocMap.from_coord(test_coordinates, x_min=0, x_max=5, y_min=0, y_max=5)
    assert with_origin.origin == [0, 0]
    assert with_origin.map == [
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '#', '.', '.', '.', '.']
    ]


def test_origin(mocked_map):
    mocked_map.origin = [-1, -2]
    mocked_map.set_position([0, 0])
    mocked_map.set_point([1, 0], 'o')
    assert mocked_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', 'o', '.', '.', '.']
    ]
    assert mocked_map.count_neighbours('.') == 3
    assert mocked_map.count_neighbours('#') == 1
    assert mocked_map.count_neighbours('o') == 1


def test_get_position(mocked_map):
    assert mocked_map.get_position() == [5, 1]


simple_moves = [
    ('U', (0, 0), (5, 0), (0, 1), (5, 1)), ('D', (0, 1), (5, 1), (0, 2), (5, 2)),
    ('R', (1, 0), (5, 0), (1, 2), (5, 2)), ('L', (0, 0), (4, 0), (0, 2), (4, 2))
]


@pytest.mark.parametrize("direction, from_00, from_50, from_02, from_52", simple_moves)
def test_one_move(mocked_map, direction, from_00, from_50, from_02, from_52):
    positions = {'00': [0, 0], '50': [5, 0], '02': [0, 2], '52': [5, 2]}
    expected = {'00': from_00, '50': from_50, '02': from_02, '52': from_52}
    for test in positions:
        mocked_map.set_position(positions[test])
        mocked_map.one_move(direction)
        assert (mocked_map.x, mocked_map.y) == expected[test]


other_moves = [
    ('U', (3, -1), (3, -1)), ('U', (2, 1), (2, 0)),
    ('D', (3, -1), (3, 0)), ('D', (3, 1), (3, 1)),
    ('R', (3, -1), (4, -1)), ('R', (4, 0), (4, 0)),
    ('L', (3, -1), (2, -1)), ('L', (-1, 0), (-1, 0)),
]


@pytest.mark.parametrize("direction, position, expected", other_moves)
def test_one_move_with_origin(mocked_map, direction, position, expected):
    mocked_map.origin = [-1, -1]
    mocked_map.set_position(position)
    mocked_map.one_move(direction)
    assert (mocked_map.x, mocked_map.y) == expected


moves = [({'U': 2, 'R': 2}, (5, 0)), ({'L': 3}, (1, 1)), ({'D': 1, 'R': -5}, (0, 2))]


@pytest.mark.parametrize("displacements, position", moves)
def test_move(mocked_map, displacements, position):
    mocked_map.set_position([4, 1])
    mocked_map.move(displacements)
    assert (mocked_map.x, mocked_map.y) == position


points = [([0, 0], '.', '.'), ([3, 1], '#', '.')]


@pytest.mark.parametrize("position, origin00, origin11", points)
def test_get_point(mocked_map, position, origin00, origin11):
    assert mocked_map.get_point(position) == origin00
    mocked_map.origin = [-1, -1]
    assert mocked_map.get_point(position) == origin11


def test_set_point(mocked_map):
    mocked_map.set_point([1, 1], '*')
    assert mocked_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '*', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    mocked_map.set_points([[2, 2], [5, 2], [4, 0]], 'o')
    assert mocked_map.map == [
        ['.', '.', '.', '.', 'o', '.'], ['.', '*', '.', '#', '#', '.'], ['#', '.', 'o', '.', '.', 'o']
    ]


neighbours = [([5, 1], 5, 3, 2), ([1, 1], 8, 7, 1)]


@pytest.mark.parametrize("position, count_total, count_dots, count_sharps", neighbours)
def test_get_neighbours(mocked_map, position, count_total, count_dots, count_sharps):
    mocked_map.set_position(position)
    test_neighbours = mocked_map.get_neighbours()
    assert len(test_neighbours) == count_total
    assert sum([n == '.' for n in test_neighbours]) == count_dots
    assert sum([n == '#' for n in test_neighbours]) == count_sharps
    assert mocked_map.count_neighbours('.') == count_dots
    assert mocked_map.count_neighbours('#') == count_sharps


neighbours = [
    ([5, 1], [[4, 0], [4, 1], [4, 2], [5, 0], [5, 2]], [[4, 1], [5, 0], [5, 2]]),
    ([1, 1], [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]], [[0, 1], [1, 0], [1, 2], [2, 1]])]


@pytest.mark.parametrize("position, all_neighbours, no_diagonals", neighbours)
def test_get_neighbours_coordinates(mocked_map, position, all_neighbours, no_diagonals):
    mocked_map.set_position(position)
    test_neighbours = mocked_map.get_neighbours_coordinates()
    for coord in all_neighbours:
        assert coord in test_neighbours
    assert position not in test_neighbours
    assert len(test_neighbours) == len(all_neighbours)
    test_neighbours_no_diagonals = mocked_map.get_neighbours_coordinates(diagonals=False)
    for coord in no_diagonals:
        assert coord in test_neighbours_no_diagonals
    assert position not in test_neighbours_no_diagonals
    assert len(test_neighbours_no_diagonals) == len(no_diagonals)


markers = [('.', 14), ('#', 4), (1, 0), ('*', 0)]


@pytest.mark.parametrize("marker, count", markers)
def test_count_marker(mocked_map, marker, count):
    assert mocked_map.count_marker(marker) == count


def test_change_marker(mocked_map):
    mocked_map.change_marker('#', 'o')
    assert mocked_map.count_marker('#') == 0
    assert mocked_map.count_marker('o') == 4
    assert mocked_map.map[1] == ['.', '.', '.', 'o', 'o', '.']


def test_apply_function(mocked_map):
    mocked_map.apply_function(lambda x: x + x)
    assert mocked_map.count_marker('.') == 0
    assert mocked_map.count_marker('..') == 14
    assert mocked_map.count_marker('##') == 4


def test_remove_lines(mocked_map):
    mocked_map.remove_lines(1)
    assert mocked_map.map == [['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']]
    mocked_map.remove_lines(1, top=False)
    assert mocked_map.map == [['.', '.', '.', '#', '#', '.']]
    mocked_map.remove_lines(12)
    assert mocked_map.map == [[]]


def test_remove_columns(mocked_map):
    mocked_map.remove_columns(1)
    assert mocked_map.map == [['.', '.', '.', '#', '.'], ['.', '.', '#', '#', '.'], ['.', '.', '.', '.', '.']]
    mocked_map.remove_columns(1, left=False)
    assert mocked_map.map == [['.', '.', '.', '#'], ['.', '.', '#', '#'], ['.', '.', '.', '.']]
    mocked_map.remove_columns(12)
    assert mocked_map.map == [[]]


def test_add_empty_lines(mocked_map):
    mocked_map.add_empty_lines(-2)
    assert mocked_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    mocked_map.add_empty_lines(2)
    assert mocked_map.map == [
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    mocked_map.add_empty_lines(2, top=False)
    assert mocked_map.map == [
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']
    ]


def test_add_empty_columns(mocked_map):
    mocked_map.add_empty_columns(-2)
    assert mocked_map.map == [
        ['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']
    ]
    mocked_map.add_empty_columns(2)
    assert mocked_map.map == [
        ['.', '.', '.', '.', '.', '.', '#', '.'], ['.', '.', '.', '.', '.', '#', '#', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.']
    ]
    mocked_map.add_empty_columns(2, left=False)
    assert mocked_map.map == [
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], ['.', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.']
    ]


submaps = [
    ([1, 1, 1, 1], [['.']]),
    ([1, 3, 0, 1], [['.', '.', '.'], ['.', '.', '#']]),
    ([4, 8, 2, 5], [['.', '.']])
]


@pytest.mark.parametrize("limits, new_map", submaps)
def test_create_submap(mocked_map, limits, new_map):
    submap = mocked_map.create_submap(limits[0], limits[1], limits[2], limits[3])
    assert submap.map == new_map


reversed_maps = [(
    False, False,
    [['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '#', '#', '.'], ['#', '.', '.', '.', '.', '.']],
    [1, 1], [5, 1]
), (
    False, True,
    [['#', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '#', '.'], ['.', '.', '.', '.', '#', '.']],
    [1, -1], [5, 1]
), (
    True, False,
    [['.', '#', '.', '.', '.', '.'], ['.', '#', '#', '.', '.', '.'], ['.', '.', '.', '.', '.', '#']],
    [-4, 1], [-3, 1]
), (
    True, True,
    [['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '.', '.', '.'], ['.', '#', '.', '.', '.', '.']],
    [-4, -1], [-3, 1]
)]


@pytest.mark.parametrize("vertical, horizontal, result_map, origin, coord", reversed_maps)
def test_reverse(mocked_map, vertical, horizontal, result_map, origin, coord):
    mocked_map.origin = [1, 1]
    mocked_map.reverse(vertical, horizontal)
    assert mocked_map.map == result_map
    assert mocked_map.origin == origin
    assert [mocked_map.x, mocked_map.y] == coord


def test_get_marker_coords(mocked_map):
    hash_positions = mocked_map.get_marker_coords('#')
    assert len(hash_positions) == 4
    assert [4, 0] in hash_positions
    assert [3, 1] in hash_positions
    assert [4, 1] in hash_positions
    assert [0, 2] in hash_positions


superpositions = [(
    work_with_maps.AocMap(['x...', '.x..', '..x.', '...x'], origin=[0, 0]),
    [
        ['x', '.', '.', '.', '#', '.'], ['.', 'x', '.', '#', '#', '.'],
        ['#', '.', 'x', '.', '.', '.'], ['.', '.', '.', 'x', '.', '.']
    ]
), (
    work_with_maps.AocMap(['x...', '.x..', '.yx.', '...x'], origin=[3, -1]),
    [
        ['.', '.', '.', 'x', '.', '.', '.'], ['.', '.', '.', '.', 'x', '.', '.'],
        ['.', '.', '.', '#', 'y', 'x', '.'], ['#', '.', '.', '.', '.', '.', 'x']
    ]
)]


@pytest.mark.parametrize("by_map, result_map", superpositions)
def test_superpose(mocked_map, by_map, result_map):
    mocked_map.superpose(by_map)
    assert mocked_map.map == result_map
