"""Solution for Question 1: Adjacency Matrix to Adjacency List"""

def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)

    Returns:
    --------
    adj_list: `list[list[int]]`
        The adjacency list of the graph

    1 - Direct approach:
    ----------------------------
    Steps:
     - Iterate through rows of matrix, iterate through each row:
       - If an element is not 0, append it's index in the row to the output row
    Notes:
     - Clearly paralelizable for every row as no prev row impacts current row behavior
     - Can't ignore half of the table because edges are directed
     - This is O(N^2) in time and O(N+#edges) in space complexity (for N=#vertices)
        - I don't see a more efficient algorithm without some magic math shortcut
    """

    # # 1 - Direct approach (using loops):
    # adj_list = []
    # for row in adj_mat:
    #     adj_list_row = []
    #     for i, val in enumerate(row):
    #         if val != 0:
    #             adj_list_row.append(i)
    #     adj_list.append(adj_list_row)
    # return adj_list

    # 1.5 - Direct approach (using list comprehension):
    return [
        [ i for i, val in enumerate(row) if val != 0 ]
        for row in adj_mat
    ]
