# def nested_array_sum(arr):
#     if isinstance(arr, int):
#        return arr       
    
#     if len(arr) == 0:
#         return 0
    
#     if not isinstance(arr[0], int):
#         value = nested_array_sum(arr[0])
#     else:
#         value = arr[0]
    
#     # remember that this indexing actually creates/allocates new array. So we do not want to be doing this.
#     return value + (nested_array_sum(arr[1:]) if len(arr) > 1 else 0)


def nested_array_sum(arr):
    total = 0
    if isinstance(arr, int):
        return arr

    for element in arr:
        total += element if isinstance(element, int) else nested_array_sum(element)

    return total
   


# Worst case of this should be 2?^n I think

def run_tests():
  tests = [
    # Example 1 from book
    ([1, [2, 3], [4, [5]], 6], 21),
    # Example 2 from book
    ([[[[1]], 2]], 3),
    # Example 3 from book
    ([], 0),
    # Edge case - single number
    (5, 5),
    # Edge case - all nested single numbers
    ([[[[[1]]]]], 1),
    # Edge case - multiple empty arrays
    ([[], [], []], 0),
    # Edge case - mixed empty and non-empty arrays
    ([[], [1, 2], [], [3]], 6),
    # Edge case - deeply nested mixed arrays
    ([1, [2, [], [3, []], []], [4, [5, []]]], 15),
    # Edge case - all zeros
    ([0, [0, 0], [0, [0]], 0], 0),
    # Edge case - negative numbers
    ([-1, [-2, 3], [4, [-5]], 6], 5),
    # Stress test - large deeply nested array
    ([list(range(10)), [list(range(10,20)), list(range(20,30))], 
      [list(range(30,40)), [list(range(40,50))]], list(range(50,60))], 
      sum(range(60)))
  ]
  for i,(arr, want) in enumerate(tests):
    got = nested_array_sum(arr)
    assert got == want, f"\nnested_array_sum({arr}): got: {got}, want: {want}\n"

if __name__ == '__main__':
   run_tests()