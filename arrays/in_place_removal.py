def  remove_duplicates(arr):
    n = len(arr)
    j = n-1
    slow, fast = 1, 1
    current = arr[0]
    while fast < n:
        if arr[fast] != current:
            arr[slow] = arr[fast]
            current = arr[fast]
            slow +=1
        fast +=1

    for i in range(slow, n):
        arr[i] = 0

    return arr 



def run_tests():
  tests = [
      # Example from the book
      ([1, 2, 2, 3, 3, 3, 5], 4, [1, 2, 3, 5]),
      # Additional test cases
      ([], 0, []),
      ([1], 1, [1]),
      ([1, 1], 1, [1]),
      ([1, 2], 2, [1, 2]),
      ([1, 1, 1], 1, [1]),
      ([1, 2, 2, 2, 3], 3, [1, 2, 3]),
  ]
  for arr, want_len, want_prefix in tests:
    arr_copy = arr.copy()  # Make a copy since remove_duplicates modifies in place
    got_len = remove_duplicates(arr_copy)
    assert got_len == want_len, \
        f"\nremove_duplicates({arr}): got length: {got_len}, want length: {want_len}\n"
    assert arr_copy[:want_len] == want_prefix, \
        f"\nremove_duplicates({arr}): got prefix: {arr_copy[:want_len]}, want prefix: {want_prefix}\n"
    
if __name__ == '__main__':
   run_tests()