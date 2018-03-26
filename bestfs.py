import search

romania_problem = search.GraphProblem('Arad', 'Craiova', search.romania_map)
#vacumm_world = search.GraphProblemStochastic('State_1', ['State_7', 'State_8'], vacumm_world)
#LRTA_problem = search.OnlineSearchProblem('State_3', 'State_5', one_dim_state_space)
eight_puzzle = search.EightPuzzle((1, 2, 3, 0, 4, 6, 7, 5, 8))
nqueens = search.NQueensProblem(8)

print("\nBest first Search")
print("\nSolution to Romania Problem Arad->Craiova")
print(search.recursive_best_first_search(romania_problem).solution())
print("\nSolution to Eight Puzzle (1, 2, 3, 0, 4, 6, 7, 5, 8)")
print(search.recursive_best_first_search(eight_puzzle).solution())