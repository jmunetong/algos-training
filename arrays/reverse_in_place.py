def reverse(arr):
    i, j = 0, len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j -=1
    
    return arr


def run_tests():
  tests = [
      # Test cases
      (list("hello"), list("olleh")),
      (list(""), list("")),
      (list("a"), list("a")),
      (list("ab"), list("ba")),
      (list("abc"), list("cba")),
      (list("abcd"), list("dcba")),
      (list("12345"), list("54321")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since reverse modifies in place
    reverse(arr_copy)
    assert arr_copy == want, f"\nreverse({arr}): got: {arr_copy}, want: {want}\n"
    
if __name__ == '__main__':
   run_tests()
