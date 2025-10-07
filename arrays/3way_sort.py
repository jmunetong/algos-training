def three_way_merge(arr1, arr2, arr3):
  
    s = set(arr1)
    for arr_i in [arr2, arr3]:
        for element in arr_i:
            if element not in s:
                s.add(element)
      

    return list(s)



def run_tests():
  tests = [
      # Example from the book
      ([2, 3, 3, 4, 5, 7], [3, 3, 9], [3, 3, 9], [2, 3, 4, 5, 7, 9]),
      # Additional test cases
      ([], [], [], []),
      ([1], [], [], [1]),
      ([1], [1], [1], [1]),
      ([1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3, 4, 5]),
      ([1, 1, 1], [1, 1], [1], [1]),
      ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
  ]
  for arr1, arr2, arr3, want in tests:
    got = three_way_merge(arr1, arr2, arr3)
    assert got == want, f"\nthree_way_merge({arr1}, {arr2}, {arr3}): got:{got}, want: {want}\n"

if __name__ == '__main__':
   run_tests()