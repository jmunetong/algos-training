def subgrid_maximums(grid):
    R = len(grid)
    C = len(grid[0])
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            grid[i][j] = max(max(grid[min(R-1, i+1)][j], grid[i][j]), grid[i][ min(C-1, j +1)])
    
    return grid
                             

def run_tests():
  tests = [
      # Example from book
      ([[1, 5, 3],
        [4, -1, 0],
        [2, 0, 2]],
       [[5, 5, 3],
        [4, 2, 2],
        [2, 2, 2]]),
      # Edge case - 1x1 grid
      ([[5]], [[5]]),
      # Edge case - single row
      ([[1, 2, 3]], [[3, 3, 3]]),
      # Edge case - single column
      ([[1], [2], [3]], [[3], [3], [3]]),
      # Edge case - negative numbers
      ([[-1, -2],
        [-3, -4]],
       [[-1, -2],
        [-3, -4]]),
      # New test case - 2x2 grid from explanation
      ([[1, 2],
        [3, 4]],
       [[4, 4],
        [4, 4]]),
  ]

  for grid, want in tests:
    got = subgrid_maximums(grid)
    assert got == want, f"\nsubgrid_maximums({grid}): got: {got}, want: {want}\n"
        
if __name__=='__main__':
   run_tests()
