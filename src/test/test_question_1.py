"""Tests for question_1.py"""

import itertools
import random
from typing import List, Tuple

import pytest

from ..question_1 import mat_to_list

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
param_cases__input_mat_and_expected_output_list = [
    (  # Example given in asssignment
        [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        [[1, 3], [2], [0], [4], [3], []],
    ),
]


@pytest.mark.parametrize(
    ["input_mat", "expected_res"], param_cases__input_mat_and_expected_output_list
)
def test_mat_to_list__in_and_out_given(
    input_mat: List[List[int]], expected_res: List[List[int]]
):
    """
    Tests the `mat_to_list` function by directly comparing its output to the
    expected result for the given input matrix.

    Args:
        input_mat (List[List[int]]): The input matrix to be converted.
        expected_res (List[List[int]]): The expected result after conversion.

    Asserts:
        The actual result from `mat_to_list` matches the expected result.
    """
    actual_res = mat_to_list(input_mat)
    assert actual_res == expected_res


# Cases for parametrization of the width of an input matrix and a list of some
# edges to include in the input.
param_cases__mat_width_and_edge_coords = (
    # Every permutation of [0..N*N] edges from N=1 to N=2 matrices:
    [
        (mat_width, coords)
        for mat_width in range(0, 3)
        for num_edges in range(0, mat_width * mat_width)
        # All "num_edges"-permutations of all the possible coordinates
        for coords in itertools.permutations(
            itertools.product(range(0, mat_width), repeat=2), num_edges
        )
    ]  # [0..10] randomly placed edges on a large matrix of N=100:
    + [
        (100, random.choices(list(itertools.permutations(range(0, 100), 2)), k=k))
        for k in range(0, 10)
    ]
)


@pytest.mark.parametrize(
    ["mat_width", "mat_edge_coords"], param_cases__mat_width_and_edge_coords
)
def test_n_random_edges_appear(mat_width: int, mat_edge_coords: List[Tuple[int, int]]):
    """
    Tests that an adjacency matrix for the given edges and is correctly converted
    to its list representation.

    Args:
        mat_width (int): The width (and height) of the square matrix.
        mat_edge_coords (List[Tuple[int, int]]): A list of tuples representing
            the coordinates of edges in the matrix.
    """
    input_mat = generate_test_mat(mat_width, mat_edge_coords)

    # Generate expected result
    expected_res = [[] for _ in range(mat_width)]
    for r, c in mat_edge_coords:
        expected_res[r].append(c)

    # Sort each expected row for safety (randomly sampled cases may not be sorted)
    for i, row in enumerate(expected_res):
        expected_res[i] = sorted(row)

    # Compare to actual result
    test_mat_to_list__in_and_out_given(input_mat, expected_res)
