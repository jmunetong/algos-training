def two_sum(arr):

    l = 0
    h = len(arr) -1
    while l < h and arr[l] <= 0 and arr[h] >= 0 :
        if arr[l] + arr[h] == 0:
            return True
        elif arr[l] + arr[h] > 0:
            h -=1
        else:
            l +=1
    
    return False



def run_tests():
  tests = [
      # Example 1 from the book
      ([-5, -2, -1, 1, 1, 10], True),
      # Example 2 from the book
      ([-3, 0, 0, 1, 2], True),
      # Example 3 from the book
      ([-5, -3, -1, 0, 2, 4, 6], False),
      # Additional test cases
      ([], False),
      ([0], False),
      ([-1, 1], True),
      ([-2, -1, 0, 1], True),
      ([1, 2, 3, 4], False),
  ]
  for arr, want in tests:
    got = two_sum(arr)
    assert got == want, f"\ntwo_sum({arr}): got: {got}, want: {want}\n"


if __name__ == '__main__':
   run_tests()