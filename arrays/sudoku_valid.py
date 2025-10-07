from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        m = 3
        is_valid_row = True
        is_valid_col = True
        is_valid_box = True
        is_valid_global = True
        for r in range(n):
            row_s = set()
            col_s = set()
            box_s = set()
            for c in range(n):
                row_element = board[r][c]
                col_element = board[c][r]

                if row_element.isdigit():
                    if row_element in row_s:
                        is_valid_row = False
                        break
                    else:
                        row_s.add(row_element)


                if col_element.isdigit():
                    if col_element in col_s:
                        is_valid_row = False
                        break
                    else:
                        col_s.add(col_element)

                box_idx_r = r//m
                box_idx_c = r % m
                b_y = m*(box_idx_c) + c % m 
                b_x = m*(box_idx_r) + c // m
                boxed_element = board[b_x][b_y]
                if boxed_element.isdigit():
                    if boxed_element in box_s:
                        is_valid_box = False
                        break
                    else:
                        box_s.add(boxed_element)
                
            if not(is_valid_box and is_valid_col and is_valid_row):
                is_valid_global = False
                break

        return is_valid_global

            
