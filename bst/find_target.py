
# Now i am going to create this problem but using a while loop
def search(arr, i, j, target):
    if i > j:
        return -1
    mid = i + (j-i)//2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return search(arr, i, mid - 1, target)
    else:
        return search(arr, mid + 1, j, target)

def solve(arr,target):
    n = len(arr)
    i = 0
    j = n -1
    while i <= j:
        mid = i + (j-i)//2 # this will allow us to check the firs telement everytime 
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    
    return -1

# def solve(arr, target):
#     return search(arr, 0, len(arr)-1, target)

def run_tests():
  tests = [
      # Example 1 from book
      ([-2, 0, 3, 4, 7, 9, 11], 3, 2),
      # Example 2 from book
      ([-2, 0, 3, 4, 7, 9, 11], 2, -1),
      # Edge case - empty array
      ([], 5, -1),
      # Edge case - target at start
      ([1, 2, 3], 1, 0),
      # Edge case - target at end
      ([1, 2, 3], 3, 2),
      # Edge case - single element
      ([5], 5, 0),
      # Edge case - not found
      ([1, 3, 5], 2, -1)
  ]

  for arr, target, want in tests:
    got = solve(arr, target)
    assert got == want, f"\nsearch_in_sorted_array({arr}, {target}): got: {got}, want: {want}\n"

if __name__ =='__main__':
    run_tests()