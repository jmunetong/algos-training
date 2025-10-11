
# computing the number of times we see the value that I am interested for this thing


# First thing that we need to do is to compute the number of times this value shows up in the list of pr

# T(n) = 2 *T(n//2) + o(1)
# T(n) = 2 * [ 2 ( T(n/4)) + o(1)] + 0(1)


# 2^{LOG(N) + C} = O(n)

def recurse_arr(arr, i, j):
    print(i,j)
    if i >= j:
        return arr[i], arr[i]
    mid = i + (j - i)//2 
    left_i, right_i = i, mid 
    left_j, right_j = mid + 1, j
    left_count, left_max = recurse_arr(arr, left_i, right_i)
    right_count, right_max = recurse_arr(arr, left_j, right_j)
    current_count = left_count + right_count
    running_max = max(max(left_max, right_max), current_count)
    return current_count, running_max



# Now let me try to build a more optimal solution for this problem
def laminal_arr(arr):
    return recurse_arr(arr, 0, len(arr)-1)[-1]


def run_tests():
  tests = [
      # Example 1 from book
      ([3, -9, 2, 4, -1, 5, 5, -4], 6),
      # Example 2 from book
      ([1], 1),
      # Example 3 from book
      ([-1, -2], -1),
      # Additional test case
      ([1, 2, 3, 4], 10),
      # Additional test case with all negatives
      ([-2, -1, -4, -3], -1),
      # Large test case
      ([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -
        12, 13, -14, 15, -16], 15),
  ]
  for i, (arr, want) in enumerate(tests):
    print(f"running test {i}")
    assert got == want, f"\nmax_laminal_sum({arr}): got: {got}, want: {want} \n"
    # got = max_laminal_sum_inefficient(arr)
    # assert got == want, f"\nmax_laminal_sum_inefficient({arr}): got: {got}, want: {want}\n"


if __name__=='__main__':
   run_tests()