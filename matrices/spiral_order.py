def spiral(n):
    val = n * n -1
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    dir = 0
    grid = [[0]*n for _ in range(n)]
    r, c = n-1, n-1
    while val >= 0:
        grid[r][c] = val
        val -=1
        r_ = r + directions[dir][0]
        c_ = c + directions[dir][1]
        if is_valid(r_, c_, grid):
            r = r_
            c = c_
        else:
            dir = (dir +1)% len(directions)
            r += directions[dir][0]
            c += directions[dir][1]

    return grid

def is_valid(r, c, grid):
    n = len(grid)
    return n > r and n > c and r >=0 and c>=0 and grid[r][c]==0

def run_tests():
  tests = [
      # Example from book
      (5, [
          [16, 17, 18, 19, 20],
          [15, 4, 5, 6, 21],
          [14, 3, 0, 7, 22],
          [13, 2, 1, 8, 23],
          [12, 11, 10, 9, 24]
      ]),
      # Edge case - 1x1
      (1, [[0]]),
      # Edge case - 3x3
      (3, [
          [4, 5, 6],
          [3, 0, 7],
          [2, 1, 8]
      ]),
  ]

  for n, want in tests:
    got = spiral(n)
    assert got == want, f"\nspiral({n}): got: {got}, want: {want}\n"


if __name__ == '__main__':
    run_tests()