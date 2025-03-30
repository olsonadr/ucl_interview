"""Solution for Question 2: Rachable Node"""


def reachable(adj_list, start_node):
    """Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node

    1 - Direct approach:
    --------------------
    Notes:
     - A node v is reachable from u either if there is an edge u->v or there is a path between them.
     - I remember you can mathematically compute the number of paths from one node to another with
       adjacency matrix (self-multiplication), but this doesn't help here and is the wrong input format.
     - There may be an easy trick for this with adjacency list. Skip this for first direct approach.
     - Use set type to avoid extra work of checking for existence of nodes in work-set/return object
       (can be implemented with hashing under the hood).
     - Could use recursion but not necessary here as iterative approach reduces risk of memory issues
       and this wouldn't provide any obvious benefits.
     - While loops always add risk, maybe consider if we could get into an infinite loop?
    Steps:
     - Initialize work_set to {start_node}
     - While work_set is not empty:
       - Pop any curr_node from work_set to consider (and mark as visited)
       - For any edge from curr_node to any other, add to work-set if not yet visited
         (prevents unbounded loop issues for cycles)
     - Return visited set (all nodes we *did* reach from start_node)
    """
    # 1 - Direct approach:
    visited = set()
    work_set = {start_node}
    while len(work_set) > 0:
        curr_node = work_set.pop()
        visited.add(curr_node)
        # Add connected+unvisited nodes to work_set
        work_set |= set(adj_list[curr_node]) - visited
    return visited
