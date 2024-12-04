import os
import sys
import pytest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools import work_with_graphs


@pytest.fixture
def mocked_graph():
    return work_with_graphs.AocGraph([
        ['start', 'A'], ['start', 'b'], ['A', 'c'], ['A', 'b'], ['b', 'a'], ['A', 'end'], ['end', 'b'],
        ['b', 'start'], ['start', 'intermediate1'], ['intermediate1', 'intermediate2'], ['intermediate2', 'c']
    ])


def test_init(mocked_graph):
    mocked_graph.nodes.sort()
    assert mocked_graph.nodes == ['A', 'a', 'b', 'c', 'end', 'intermediate1', 'intermediate2', 'start']


paths = [(['A', 'start'], True), (['a', 'A'], False)]


@pytest.mark.parametrize("path, exists", paths)
def test_init_paths(mocked_graph, path, exists):
    assert ((path in mocked_graph.paths) == exists) | (([path[1], path[0]] in mocked_graph.paths) == exists)


neighbourhood = [
    ('A', ['b', 'c', 'end', 'start'],  ['c', 'end', 'start']), ('end', ['A', 'b'], ['A']), ('a', ['b'], []),
    ('e', [], []), ('c', ['A', 'intermediate2'], ['A', 'intermediate2'])
]


@pytest.mark.parametrize("node, neighbours, bForbidden", neighbourhood)
def test_get_neighbours(mocked_graph, node, neighbours, bForbidden):
    test_neighbours = mocked_graph.get_neighbours(node)
    test_neighbours.sort()
    assert test_neighbours == neighbours
    mocked_graph.forbid_node('b')
    test_neighbours_available_only = mocked_graph.get_neighbours(node, True)
    test_neighbours_available_only.sort()
    assert test_neighbours_available_only == bForbidden


def test_forbid_node(mocked_graph):
    assert 'A' not in mocked_graph.forbidden
    mocked_graph.forbid_node('A')
    assert 'A' in mocked_graph.forbidden


c = [
    ('start', 2, 3), ('c', 0, 0), ('A', 1, None), ('b', 2, 4), ('a', 3, 5), ('e', None, None)
]


@pytest.mark.parametrize("node, distance, Aforbidden", c)
def test_distance(mocked_graph, node, distance, Aforbidden):
    assert mocked_graph.distance('c', node) == distance
    assert mocked_graph.distance(node, 'c') == distance
    mocked_graph.forbid_node('A')
    assert mocked_graph.distance('c', node, available_only=True) == Aforbidden
    assert mocked_graph.distance(node, 'c', available_only=True) == Aforbidden


def test_count_paths(mocked_graph):
    assert work_with_graphs.count_paths(mocked_graph, 'start', 'end') == 6
    assert work_with_graphs.count_paths(mocked_graph, 'start', 'end', forbidden=['A']) == 1
    assert work_with_graphs.count_paths(mocked_graph, 'start', 'end', forbidden=['b']) == 2

