def safe_cells(board):
    n= len(board)
    grid = [[0]*n for _ in range(n)]
    queens_idx_list = search_queens(board, grid)
    for queen_idx in queens_idx_list:
        r, c = queen_idx[0], queen_idx[1]
        coordinates = kings_move(grid, r,c)

        for coordinate in coordinates:
            r_, c_ = coordinate[0], coordinate[1]
            diff_x, diff_y = r_ - r, c_ - c
            r_+=diff_x
            c_ += diff_y
            while is_valid(grid, r_, c_):
                grid[r_][c_] = 1
                r_ += diff_x
                c_ += diff_y
    return grid


def search_queens(board, grid):
    idx = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] ==1:
                idx.append([i,j])
                grid[i][j] = 1
    return idx

def kings_move(grid, r, c):
    coordinates = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i ==0 and j ==0:
                continue
            r_ = r + i
            c_ = c + j
            if is_valid(grid, r_, c_):
                grid[r_][c_] = 1
                coordinates.append([r_, c_])
    return coordinates

def is_valid(grid, r_, c_):
    n = len(grid)
    return n> r_ and n > c_ and r_ >= 0 and c_>=0 and grid[r_][c_] ==0



def run_tests():
  tests = [
      ([[0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]],
       [[1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]),
      # Edge case - empty board
      ([], []),
      # Edge case - 1x1 board with queen
      ([[1]], [[1]]),
      # Edge case - 1x1 board without queen
      ([[0]], [[0]]),
      # Edge case - no queens
      ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
  ]

  for board, want in tests:
    got = safe_cells(board)
    assert got == want, f"\nsafe_cells({board}): got: {got}, want: {want}\n"

if __name__ == '__main__':
    run_tests()