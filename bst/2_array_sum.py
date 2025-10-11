def solve(arr_s, arr_us):
    
    def _search_bst(arr_s, target) :

        i = 0
        j = len(arr_s) -1
        while i <= j:
            mid = i + (j-i + 1)//2
            difference = target + arr_s[mid]
            if difference == 0:
                return mid
            elif difference > 0:
                j = mid - 1
            else:
                i = mid + 1
    
        return -1

    for k in range(len(arr_us)): 
        sorted_idx = _search_bst(arr_s, arr_us[k])
        if sorted_idx != -1:
            return [sorted_idx, k]
    return [-1, -1]


# Assuming we have an unsorted array of shape M and a sorted array of shape N,
# the for loop will run O(M). Now the sorted array for each unsorted value, will run in the order of O(N).

# One question that i have is whether we can figure out a way to make these values from the searching faster. 

def run_tests():
  tests = [
      # Example from book
      ([-5, -4, -1, 4, 6, 6, 7], [-3, 7, 18, 4, 6], [1, 3]),
      # no solution
      ([1, 2, 3], [1, 2, 3], [-1, -1]),
      ([1], [-1], [0, 0]),
      ([1, 2], [-2, -1], [1, 0]),
      ([0, 1, 2, 3], [3, 2, 1, 0], [0, 3]),
  ]

  for sorted_arr, unsorted_arr, want in tests:
    got = solve(sorted_arr, unsorted_arr)
    assert got == want, f"\ntwo_array_two_sum({sorted_arr}, {unsorted_arr}): got: {got}, want: {want}\n"


if __name__ =='__main__':
    run_tests()
    
