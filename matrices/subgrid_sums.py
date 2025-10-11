def subgrid_sums(grid):
    R = len(grid)
    C = len(grid[0])
    out_grid = [[0]* C for _ in range(R)]
    out_grid[R-1][C-1] = grid[R-1][C-1]
    for r in range(R-1, -1,-1):
       for c in range(C-1, -1, -1):
            out_grid[r][c] = grid[r][c]
        
            if r +1 < R:
                out_grid[r][c] += (out_grid[r+1][c])
            
            if c + 1 < C:
                out_grid[r][c] += (out_grid[r][c+1])

            if c +1 < C and r+1 < R:
                out_grid[r][c] -= out_grid[r+1][c+1]
  
    return out_grid


                             

def run_tests():
  tests = [
      # Example from book
      ([[-1, 2, 3],
        [4, 0, 0],
        [-2, 0, 9]],
       [[15, 14, 12],
        [11, 9, 9],
        [7, 9, 9]]),
      # Edge case - 1x1 grid
      ([[5]], [[5]]),
      # Edge case - single row
      ([[1, 2, 3]], [[6, 5, 3]]),
      # Edge case - single column
      ([[1], [2], [3]], [[6], [5], [3]]),
      # Edge case - all zeros
      ([[0, 0],
        [0, 0]],
       [[0, 0],
        [0, 0]]),
  ]

  for grid, want in tests:
    got = subgrid_sums(grid)
    assert got == want, f"\nsubgrid_sums({grid}): got: {got}, want: {want}\n"
        
if __name__=='__main__':
   run_tests()
