import search

romania_problem = search.GraphProblem('Arad', 'Bucharest', search.romania_map)
#vacumm_world = search.GraphProblemStochastic('State_1', ['State_7', 'State_8'], vacumm_world)
#LRTA_problem = search.OnlineSearchProblem('State_3', 'State_5', one_dim_state_space)
eight_puzzle = search.EightPuzzle((1, 2, 3, 0, 4, 6, 7, 5, 8))
nqueens = search.NQueensProblem(8)



print("\n\nBreadth first search\n")

def breadth_first_search(problem):
    """[Figure 3.11]
	Note that this function can be implemented in a 
	single line as below:
	return graph_search(problem, FIFOQueue())
    """
    node = search.Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = search.FIFOQueue()
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        explored.add(tuple(node.state))
        for child in node.expand(problem):
            if child.state not in tuple(explored) and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None
print("Solution for 8 QUEENS : ")
print(breadth_first_search(nqueens).solution())
print("\n\nSolution for 8 Puzzle (1, 2, 3, 0, 4, 6, 7, 5, 8) : ")
print(breadth_first_search(eight_puzzle).solution())
