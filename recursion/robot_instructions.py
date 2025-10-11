
def moves(instruction):
    if len(instruction) <=1:
        return instruction
        
    if instruction[0] == '2':
        return moves(instruction[1:]) + moves(instruction[2:]) 
    else:
        return instruction[0] + moves(instruction[1:]) 



def run_tests():
    tests = [
    # Example 1 from book
    ("LL", "LL"),
    # Example 2 from book
    ("2LR", "LRR"),
    # Example 3 from book
    ("2L", "L"),
    # Example 4 from book
    ("22LR", "LRRLR"),

    # All instructions after:
    # 22LR -> Working on first 2: 2LR LR -> LRRLR (This is the outcome of this value)
    # Example 5 from book
    ("LL2R2L", "LLRLL"),
    # Edge case - empty string
    ("", ""),
    # Edge case - single character
    ("L", "L"),
    # Multiple 2s in a row
    ("2222LR", "LRRLRLRRLRRLR"),
    ]

    for seq, want in tests:
        got = moves(seq)
        assert got == want, f"\nmoves({seq}): got: {got}, want: {want}\n"

if __name__ == '__main__':
    run_tests