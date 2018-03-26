from utils import (
    is_in, argmin, argmax, argmax_random_tie, probability, weighted_sampler,
    memoize, print_table, open_data, Stack, FIFOQueue, PriorityQueue, name,
    distance, vector_add
)
import search

eight_puzzle = search.EightPuzzle((1, 2, 3, 0, 4, 6, 7, 5, 8))
nqueens = search.NQueensProblem(8)
def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return search.best_first_graph_search(problem, lambda n: n.path_cost + h(n))

print("A-Star Solution for 8 Puzzle (1, 2, 3, 0, 4, 6, 7, 5, 8) ")
print(astar_search(eight_puzzle).solution())

