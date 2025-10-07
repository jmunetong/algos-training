def merge(arr1, arr2):

    n1 = len(arr1)
    n2 = len(arr2)

    i = 0 # pointer to arr1
    j = 0 # pointer to arr2

    final_arr = []
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            final_arr.append(arr1[i])
            i += 1
        else:
            final_arr.append(arr2[j])
            j +=1

    while i < n1:
        final_arr.append(arr1[i])
        i+=1

    while j < n2:
        final_arr.append(arr2[j])
        j+=1

    return final_arr


        

def run_tests():
  tests = [
      # Example 1 from the book
      ([1, 3, 4, 5], [2, 4, 4], [1, 2, 3, 4, 4, 4, 5]),
      # Example 2 from the book
      ([-1], [], [-1]),
      # Additional test cases
      ([], [], []),
      ([1], [], [1]),
      ([], [1], [1]),
      ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
      ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
  ]
  for arr1, arr2, want in tests:
    got = merge(arr1, arr2)
    assert got == want, f"\nmerge({arr1}, {arr2}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests