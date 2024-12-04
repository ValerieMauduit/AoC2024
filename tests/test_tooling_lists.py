import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import work_with_lists


@pytest.fixture
def test_data():
    return [12, 42, 73, 1]


sliding_data = [(
    [12, 42, 73, 1], 2, [[12, 42], [42, 73], [73, 1]]
), (
    [12, 42, 73, 1], 3, [[12, 42, 73], [42, 73, 1]]
), (
    'abcdefg', 3, ['abc', 'bcd', 'cde', 'def', 'efg']
)]


@pytest.mark.parametrize("data, span, result", sliding_data)
def test_sliding_windows(data, span, result):
    assert work_with_lists.sliding_windows(data, size=span) == result


strings = [('abc', ['a', 'b', 'c']), ('aa', ['a', 'a']), ('', [])]


@pytest.mark.parametrize("from_string, to_list", strings)
def test_str_to_list(from_string, to_list):
    assert work_with_lists.str_to_list(from_string) == to_list


positions = [(['a', 'b', 'c'], [1]), (['a', 'b', 'b', 'c', 'c', 'b'], [1, 2, 5]), (['b'], [0]), (['a', 'c'], [])]


@pytest.mark.parametrize('in_list, b_indexes', positions)
def test_positions(in_list, b_indexes):
    assert work_with_lists.positions('b', in_list) == b_indexes


@pytest.mark.parametrize('in_list, b_indexes', positions)
def test_count_values(in_list, b_indexes):
    assert work_with_lists.count_value('b', in_list) == len(b_indexes)


least_and_most = [(
    ['N', 'B', 'B', 'B', 'N', 'N', 'C', 'C', 'N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'C', 'H', 'B', 'H', 'H', 'B', 'C'],
    None,
    ['B', 10], ['H', 3]
), (
    ['N', 'B', 'B', 'B', 'N', 'N', 'C', 'C', 'N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'C', 'H', 'B', 'H', 'H', 'B', 'C'],
    ['N', 'B', 'C'],
    ['B', 10], ['C', 4]
), (
    ['N', 'B', 'B', 'B', 'N', 'N', 'C', 'C', 'N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'C', 'H', 'B', 'H', 'H', 'B', 'C'],
    ['A', 'Q', 'C'],
    ['C', 4], ['A', 0]
), (
    ['N', 'B', 'B', 'B', 'N', 'N', 'C', 'C', 'N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'C', 'H', 'B', 'H', 'H', 'B', 'C'],
    ['V', 'M', 'A'],
    [None, 0], ['V', 0]
), (
    [], None, [None, 0], [None, 1]
)]


@pytest.mark.parametrize('from_list, values, most, least', least_and_most)
def test_least_and_most(from_list, values, most, least):
    assert work_with_lists.most_common(from_list, values) == most
    assert work_with_lists.least_common(from_list, values) == least


def test_merge_lists():
    assert work_with_lists.merge_lists(['a', 'b', 'c'], ['d', 'e', 'f']) == ['a', 'd', 'b', 'e', 'c', 'f']
