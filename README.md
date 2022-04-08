# squareword-minimum-brute-force
A very basic brute force algorithm for finding squareword grids that can potentially be solved in the fewest possible guesses. The algorithm will output candidates for grids that can be solved in x guesses, where x iteratively increases. These candidate grids will consist of a valid squareword grid (all horizontal and vertical lines are words in the built-in word list) such that the vertical words all contain no greater than x distinct letters. However, this does not guarantee that the grid can actually be solved in x guesses.