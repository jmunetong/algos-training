def prefix_suffix_swap(arr):

    N = len(arr)
    p_len = int(N/3)
    # replace overlapping elements
    i = 0
    j = -p_len
    while i < p_len:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j +=1

    k =0
    while k < p_len:
        arr[k], arr[p_len +k] =  arr[p_len +k], arr[k]
        k+=1
    return arr

s = 'badreview'
print(prefix_suffix_swap(list(s)))

def run_tests():
  tests = [
      # Example from the book
      (list("badreview"), list("reviewbad")),
      # Additional test cases
      ([], []),
      (list("abc"), list("bca")),
      (list("abcdef"), list("cdefab")),
      (list("123456789"), list("456789123")),
      (list("aaabbbccc"), list("bbbcccaaa")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since swap_prefix_suffix modifies in place
    prefix_suffix_swap(arr_copy)
    assert arr_copy == want, f"\nswap_prefix_suffix({arr}): got: {arr_copy}, want: {want}\n"

if __name__ == '__main__':
   run_tests()