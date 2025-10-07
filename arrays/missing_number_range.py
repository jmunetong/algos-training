def missing_numbers_range(arr, low, high):

    i = 0
    N = len(arr)
    result = []
    current = low

    while i < N:
        if arr[i] < low or current > arr[i]:
            i +=1
            continue
        
        if arr[i] > high:
            break

        while current < arr[i]:
            result.append(current)
            current +=1

        current +=1
        i+=1

    if current <= high:
        for i in range(current, high+1):
            result.append(i)
    
    return result            


def test_missing_numbers_range():
    def assert_equal(result, expected, case):
        assert result == expected, f"Test failed: {case}\nExpected: {expected}, but got: {result}"

    # Test cases: (arr, low, high, expected_output)
    test_cases = [
        ([1, 3, 5], 1, 5, [2, 4]),                    # missing numbers in between
        ([1, 2, 3, 4, 5], 1, 5, []),                   # full range covered
        ([], 1, 5, [1, 2, 3, 4, 5]),                   # empty input array
        ([2, 4, 6, 8], 1, 8, [1, 3, 5, 7]),            # alternating missing values
        ([10, 12, 15], 10, 15, [11, 13, 14]),          # non-contiguous range
        ([5, 7, 10], 5, 10, [6, 8, 9]),                # sparse coverage
        ([1, 1, 2, 2, 3], 1, 3, []),                   # duplicates, still sorted
        ([1, 1, 3, 4], 1, 4, [2]),                     # one missing value
        ([100, 101, 105], 100, 105, [102, 103, 104]),  # high-value range
        ([0], 0, 0, []),                               # single value, exact match
        ([1], 0, 2, [0, 2]),                           # range wider than input

        ([6, 9, 12, 15, 18], 9, 13, [10, 11, 13]),
      # Example 2 from the book
      ([], 9, 9, [9]),
      # Example 3 from the book
      ([6, 7, 8, 9], 7, 8, []),
      # Additional test cases
      ([], 1, 5, [1, 2, 3, 4, 5]),
      ([1, 2, 3, 4, 5], 1, 5, []),
      ([1, 3, 5], 1, 5, [2, 4]),
      ([1], 1, 1, []),
      ([2], 1, 3, [1, 3]),
    ]

    for idx, (arr, low, high, expected) in enumerate(test_cases, 1):
        print(arr)
        result = missing_numbers_range(arr, low, high)
        assert_equal(result, expected, f"Case #{idx}: missing_numbers_range({arr}, {low}, {high})")

    print("All test cases passed!")

if __name__ == '__main__':
    test_missing_numbers_range()
