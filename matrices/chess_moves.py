# Board (nxn) such that n>0 and we have that 0 denotes an empty cell and 1 denotes an occupied cell
#piece, which is either a king, knight or queen
# 0<=r< n and 0<=c<n
# our goal is to return a list of all unocupied cells in the board that can be reached by the given piece in one move starting from [r,c]. The order of the output cell does not matter
import math
def check_boundaries(r_next, c_next, n):
    return n > r_next and n > c_next and r_next >=0 and c_next>=0
 

def is_valid(board, r_next, c_next, n):
    # that the bound is not out of the boundary and not occupied
    return check_boundaries(r_next,c_next, n) and board[r_next][c_next] ==0  


def knight_moves(board, r, c):
    n = len(board) # I will be assuming that the shape of board is actually square such that w=h=n
    min_move = -2
    max_move = 2
    coordinates = []
    for i in range(min_move, max_move+1):
        if i==0:
            continue
        c_moves = 1 + (max_move - abs(i))
        for j in range(-c_moves, c_moves + 1, 2 * c_moves):
            if is_valid(board, r+i, c+j, n):
                coordinates.append([r+i,c + j])

    return coordinates

def king_moves(board, r, c):
    n = len(board)
    coordinates = []
    min_range = -1
    max_range = 1
    for i in range(min_range, max_range + 1):
        for j in range(min_range, max_range +1):
            if i==0 and j==0:
                continue
            if is_valid(board, r+i, c+j, n):
                coordinates.append([r+i, c+j])
    
    return coordinates


def queen_moves(board, r, c):
    n = len(board) # I will be assuming that the shape of board is actually square such that w=h=n
    coordinates = king_moves(board, r, c)
    next_coordinates = []
    for coordinate in coordinates:
        r_, c_ = coordinate[0], coordinate[1]
        diff_x, diff_y = r_ - r, c_ - c
        r_ += diff_x
        c_ += diff_y
        while is_valid(board, r_, c_, n):
            next_coordinates.append([r_, c_])
            r_ +=diff_x
            c_ += diff_y
    coordinates.extend(next_coordinates)
    return coordinates


functions = {"knight": knight_moves,
             "queen": queen_moves,
             "king": king_moves}

def chess_moves(board, piece, r, c):
    return functions[piece](board, r, c)






def run_tests():
  tests = [
    #   Example 1 from the book - king moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "king", 3, 5,
          [[2, 5], [3, 4], [4, 4], [4, 5]]),
      # Example 2 from the book - knight moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "knight", 4, 3,
       [[2, 2], [3, 5], [5, 5]]),
      # Example 3 from the book - queen moves
      ([[0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]], "queen", 4, 4,
       [[3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5],
        [5, 3], [5, 4], [5, 5]]),
      # Edge case - 1x1 board
      ([[0]], "queen", 0, 0, []),
      # Edge case - all occupied except current position
      ([[1, 1], [1, 0]], "knight", 1, 1, []),
  ]

  for i, (board, piece, r, c, want) in enumerate(tests):
    got = chess_moves(board, piece, r, c)
    # Sort both lists for consistent comparison
    got.sort()
    want.sort()
    assert got == want, (f"Failed test: {i} \nchess_moves({board}, {piece}, {r}, {c}): "
                         f"got: {got}, want: {want}\n")
    
if __name__ =='__main__':
    run_tests()