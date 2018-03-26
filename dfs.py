import search

eight_puzzle = search.EightPuzzle((1, 2, 3, 4, 5, 7, 8, 6, 0))
nqueens = search.NQueensProblem(8)

def breadth_first_tree_search(problem):
    """Search the shallowest nodes in the search tree first."""
    return tree_search(problem, FIFOQueue())


def tree_search(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinites in case of loops. [Figure 3.7]"""
    frontier.append(Node(problem.initial))
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

print("\nDepth first search")

print("\nSolution for 8 QUEENS : ")
print(search.depth_first_tree_search(nqueens).solution())