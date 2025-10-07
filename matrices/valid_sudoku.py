def valid_sudoku(board):
    return solve_cols(board) and solve_rows(board) and solve_sub_grids(board)

def solve_rows(board):
    Rows, Cols = len(board), len(board[0])
    unique_vals = set()
    for r in range(Rows): 
        unique_vals = set()
        for c in range(Cols):
            element = board[r][c]
            if element !=0:
                if element not in unique_vals:
                    unique_vals.add(element)
                else:
                    return False
    
    return True

def solve_sub_grids(board):
    Rows, Cols = len(board), len(board[0])
    stride = 3
    n_rows = Rows//stride
    n_cols = Cols//stride
    for i in range(n_rows):
        start_row = i * stride
        for j in range(n_cols):
            start_col = j * stride
            unique_box_set = set()
            for i_s in range(stride):
                for j_s in range(stride):
                    r_ = start_row + i_s
                    c_ = start_col + j_s
                    element = board[r_][c_]
                    if element != 0:
                        if element in unique_box_set:
                            return False
                        
                        unique_box_set.add(element)
    return True
                    


def solve_cols(board):
    Rows, Cols = len(board), len(board[0])
    unique_vals = set()
    for c in range(Cols): 
        unique_vals = set()
        for r in range(Rows):
            element = board[r][c]
            if element !=0:
                if element not in unique_vals:
                    unique_vals.add(element)
                else:
                    return False
    
    return True


def run_tests():
  tests = [
      # Example 1 from book - valid sudoku
      ([[5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 0, 5, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 8, 0, 2, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7]], True),
      # Example 2 from book - invalid sudoku (duplicate 7 in bottom right subgrid)
      ([[5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 0, 5, 0, 3, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 3],
        [0, 0, 0, 3, 0, 0, 0, 4, 0],
        [0, 0, 3, 0, 8, 0, 7, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7]], False),
      # Edge case - empty board
      ([[0] * 9 for _ in range(9)], True),
      # Edge case - full valid board
      ([[1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 5, 6, 4, 8, 9, 7],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [8, 9, 7, 2, 3, 1, 5, 6, 4],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [6, 4, 5, 9, 7, 8, 3, 1, 2],
        [9, 7, 8, 3, 1, 2, 6, 4, 5]], True),
  ]


  for board, want in tests:
    got = valid_sudoku(board)
    assert got == want, f"\nsolve({board}): got: {got}, want: {want}\n"

if __name__ =='__main__':
    print("here")
    run_tests()