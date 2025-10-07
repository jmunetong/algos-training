class Solution:
    def convert(self, s: str, numRows: int) -> str:
        total_length = len(s)
        if numRows==1 or numRows >= total_length:
            return s
        string_row_c = [''] * numRows
        current_row = 0
        down = False
        for char in s:
            string_row_c[current_row] +=char
            if current_row == 0 or current_row == numRows-1:
                down = not down
            
            current_row += 1 if down else -1
        return ''.join(string_row_c)