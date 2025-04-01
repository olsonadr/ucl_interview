"""Tests for question_2.py"""

from typing import List, Set, Tuple

import pytest

from ..question_2 import reachable

## Helpers


def generate_test_mat(
    mat_width: int, mat_edge_coords: List[Tuple[int, int]]
) -> List[List[int]]:
    """
    Generates a square matrix of given width with specified edge coordinates marked.
    Args:
        mat_width (int): The width (and height) of the square matrix.
        mat_edge_coords (List[Tuple[int, int]]): A list of tuples representing the
            coordinates (row, col) to be marked with 1 in the matrix.
    Returns:
        List[List[int]]: A 2D list representing the generated matrix, where cells
        at the specified edge coordinates are marked with 1, and all other cells
        are 0.
    """
    return [
        [1 if (row, col) in mat_edge_coords else 0 for col in range(mat_width)]
        for row in range(mat_width)
    ]


## Tests


# Cases for parametrization of the input matrix and expected output list.
param_cases__input_adj_list_and_expected_output_set = [
    (  # Examples given in asssignment
        [[1, 3], [2], [0], [4], [3], []],
        0,
        {0, 1, 2, 3, 4},
    ),
    (
        [[1, 3], [2], [0], [4], [3], []],
        3,
        {3, 4},
    ),
]


@pytest.mark.parametrize(
    ["input_adj_list", "input_start_node", "expected_res"],
    param_cases__input_adj_list_and_expected_output_set,
)
def test_reachable__in_and_out_given(
    input_adj_list: List[List[int]], input_start_node: int, expected_res: Set[int]
):
    """
    Tests the `reachable` function by directly comparing its output to the
    expected result for the given input adjacency list.

    Args:
        input_adj_list (List[List[int]]): The input adjacency list to be processed.
        expected_res (Set[int]): The expected result of reachable nodes.

    Asserts:
        The actual result from `reachable` matches the expected result.
    """
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res


# Specialized tests for edge cases and additional scenarios for `reachable`


def test_reachable__empty_graph():
    """
    Test `reachable` with an empty graph (no nodes).
    """
    input_adj_list = []
    input_start_node = 0
    expected_res = set()
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res


def test_reachable__single_node_no_edges():
    """
    Test `reachable` with a single node graph with no edges.
    """
    input_adj_list = [[]]
    input_start_node = 0
    expected_res = {0}
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res


def test_reachable__disconnected_graph():
    """
    Test `reachable` with a graph where nodes are disconnected.
    """
    input_adj_list = [[], [], []]
    input_start_node = 1
    expected_res = {1}
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res


def test_reachable__cyclic_graph():
    """
    Test `reachable` with a cyclic graph.
    """
    input_adj_list = [[1], [2], [0]]
    input_start_node = 0
    expected_res = {0, 1, 2}
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res


def test_reachable__self_loop():
    """
    Test `reachable` with a graph containing a self-loop.
    """
    input_adj_list = [[0], [2], []]
    input_start_node = 1
    expected_res = {1, 2}
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res


def test_reachable__large_graph():
    """
    Test `reachable` with a larger graph to ensure scalability.
    """
    input_adj_list = [[1, 2], [3], [3, 4], [5], [5], []]
    input_start_node = 0
    expected_res = {0, 1, 2, 3, 4, 5}
    actual_res = reachable(input_adj_list, input_start_node)
    assert actual_res == expected_res
