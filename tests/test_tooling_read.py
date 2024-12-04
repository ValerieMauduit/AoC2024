import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import read_data


@pytest.fixture
def test_line():
    return "20-22, 21-87"


def test_read_data_without_split():
    assert read_data.read_data('tests/input_test.txt', numbers=True, by_block=True) == [[12, 156], [1], [42, 42, 3]]
    assert read_data.read_data('tests/input_test.txt', numbers=True, by_block=False) == [12, 156, 1, 42, 42, 3]
    assert (read_data.read_data('tests/input_test.txt', numbers=False, by_block=False) ==
            ['12', '156', '', '1', '', '42', '42', '3'])
    assert (read_data.read_data('tests/input_test.txt', numbers=False, by_block=True) ==
            [['12', '156'], ['1'], ['42', '42', '3']])


def test_read_data_with_split():
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=True, split=' ') ==
            [[12, 13, 14], [1, 2, 3], ['45-42'], [67]])
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=False, split=' ') ==
            [['12', '13', '14'], ['1', '2', '3'], ['45-42'], ['67']])
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=True, split='-') ==
            [['12 13 14'], ['1 2 3'], [45, 42], [67]])
    assert (read_data.read_data('tests/input_test_for_splits.txt', numbers=False, split='-') ==
            [['12 13 14'], ['1 2 3'], ['45', '42'], ['67']])
    with pytest.raises(Exception) as exc_info:
        read_data.read_data('tests/input_test_for_splits.txt', by_block=True, split='-')
    assert len(exc_info.value.args[0]) > 0


def test_smart_split(test_line):
    assert read_data.smart_split(test_line, "-|, ") == ["20", "22", "21", "87"]
    assert read_data.smart_split([test_line, test_line], "-|, ") == [["20", "22", "21", "87"], ["20", "22", "21", "87"]]
