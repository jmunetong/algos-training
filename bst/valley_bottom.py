def solve(arr):
    left = 0
    right = len(arr)-1
    while right - left > 1:
        mid =left + (right - left)//2
        if arr[left] > arr[right]:
            left = mid
        else:
            right = mid
    
    return arr[left] if arr[left]<arr[right] else arr[right]

def run_tests():
  tests = [
      # Example 1 from book
      ([6, 5, 4, 7, 9], 4),
      # Example 2 from book
      ([5, 6, 7], 5),
      # Example 3 from book
      ([7, 6, 5], 5),
      # Edge case - 2 elements
      ([2, 1], 1),
      # Edge case - 3 elements
      ([3, 2, 4], 2)
  ]

  for arr, want in tests:
    got = solve(arr)
    assert got == want, f"\nvalley_bottom({arr}): got: {got}, want: {want}\n"


if __name__ =='__main__':
   run_tests()
# use two pointers for this problem
# left side goes down
# right side, goes up
# we need to look at this inflection point

# compare a[left] a[right]. If one is larger than the other then we should decrease the larger. Remember that the smallest element is always in the middle

# If this is the case the brute force approach would be to loop throguh the entire list until we see a value that changes from decreasing to increasing and stop right there.# This could take on the order of O(N)'

# however we could do far better than this as follows:
#using binary search
