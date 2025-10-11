
def solve(n, ls=[1, 1]):
    num_vals = len(ls)
    if n <= 1:
        return ls[n]
    if n-1 >= num_vals:
        ls.append(solve(n-1, ls))
    return ls[n-1] + ls[n-2]
    
def run_tests():
    tests = [
        # Base cases
        (1, 1),  # Only one way: one 1x1 tile
        (2, 2),  # Two ways: two 1x1 tiles OR one 2x1 tile
        (3, 3),  # Three ways: 1+1+1, 2+1, 1+2
        (4, 5),  # Five ways: 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2
        (5, 8),  # Fibonacci continues
        
        # Medium cases
        (6, 13),
        (7, 21),
        (8, 34),
        (10, 89),
        
        # Larger cases
        (15, 987),
        (20, 10946),
        
        # Edge case for potential overflow/performance
        (30, 1346269),
    ]

    for i , (n, want) in enumerate(tests):
        got = solve(n)
        assert got == want, f"\nsolve({n}): got: {got}, want: {want} in test {i+1}\n"

if __name__ == '__main__':
    run_tests()