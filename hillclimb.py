
import search
from utils import (
    is_in, argmin, argmax, argmax_random_tie, probability, weighted_sampler,
    memoize, print_table, open_data, Stack, FIFOQueue, PriorityQueue, name,
    distance, vector_add
)
eight_puzzle = search.EightPuzzle((1, 2, 3, 4, 5, 7, 8, 6, 0))
nqueens = search.NQueensProblem(8)
romania_problem = search.GraphProblem('Arad', 'Craiova', search.romania_map)

prob = search.PeakFindingProblem((0, 0), [[0, 5, 30, 20],[10, 5, 45, 20],[6,9,18,22]])
print(search.hill_climbing(prob))