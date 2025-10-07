

def smaller_prefixes(arr):
    N = len(arr)
    if N == 0:
        return True
    
    i = 0
    j = 0
    sum_i = 0
    sum_j = 0
    while j < N:
        sum_i += arr[i]
        sum_j += arr[j] + arr[j+1]
        i +=1
        j +=2
        if sum_i >= sum_j:
            return False
    return True



def run_tests():
  tests = [
      # Example 1 from the book
      ([1, 2, 2, -1], True),
      # Example 2 from the book
      ([1, 2, -2, 1, 3, 5], False),
      # Additional test cases
      ([0, 3, 7, 12, 10, 5, 0, 1], True),
      ([], True),
      ([1, 2], True),
      ([2, 1], True),
      ([-2, 1, -4, 5, -3, 7], True),
      ([-2, 1, -14, 8, -3, 2], False),
  ]
  for arr, want in tests:
    got = smaller_prefixes(arr)
    assert got == want, f"\nsmaller_prefixes({arr}): got: {got}, want: {want}\n"



if __name__ == '__main__':
   run_tests()