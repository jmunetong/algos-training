def distance_to_river(grid):
    dist = len(grid)  
    n_rows = dist
    for i in range(n_rows):
        if grid[i][0] ==1:
            r = i
            dist = r
            break
    
    n_cols = len(grid[0])
    for j in range(1, n_cols):
        for r_ in range(max(0,r-1), min(r + 2, n_rows)):
            if grid[r_][j] == 1:
                dist = min(dist, r_)
                r = r_
    return dist


def run_tests():
  tests = [
      # Example from book
      ([[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1]], 1),
      # Edge case - top of grid
      ([[1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]], 0),
      # Edge case - bottom of grid
      ([[0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]], 2),
      # Edge case - single column
      ([[0], [1], [0]], 1),
      # Edge case - single row
      ([[1]], 0),
      # Edge case - zigzag path
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1]], 1),
      # Test max up/down movement
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]], 1),
      # Test staying at same level
      ([[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]], 1),
      # Test going up then down
      ([[0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]], 1)
  ]

  for field, want in tests:
    got = distance_to_river(field)
    assert got == want, f"\ndistance_to_river({field}): got: {got}, want: {want}\n"
    
if __name__=='__main__':
    run_tests()
# careful because we need ot check that we have all the values vailable to us