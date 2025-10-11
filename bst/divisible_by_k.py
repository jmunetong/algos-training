# I will be thinking about a way to solving this by 
def solve(arr, target, k):
    def _search(arr, target):
        i = 0
        j = len(arr)-1

        # how about thinking the values in different ordering

        while i <=j:
            mid = i + (j - i + 1)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return -1


    # i will be assumming that the number is always found in this list
    idx_point = _search(arr, target)
    if idx_point == -1:
        return True
    
    count = 1
    i = idx_point - 1
    j = idx_point + 1

    while i >=0 and arr[i] == target:
        count +=1
        i -=1

    while j < len(arr) and arr[j] == target:
        count +=1
        j +=1

    return count % k ==0
    

def run_tests():
  tests = [
      # Example 1
      ([1, 2, 2, 2, 2, 2, 2, 3], 2, 3, True),
      # Example 2
      ([1, 2, 2, 2, 2, 2, 2, 3], 2, 4, False),
      # Example 3: 0 occurrences, 0 is multiple of any number
      ([1, 2, 2, 2, 2, 2, 2, 3], 4, 3, True),
      # Example 4
      ([1, 1, 2, 2, 2], 1, 3, False),
      # Edge case - empty array
      ([], 1, 2, True),
      # single occurrence, at the start
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2, False),
      # single occurrence, at the end
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 2, False),
      # single occurrence, in the middle
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 2, False),
      # smaller than any elements
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 2, True),
      # larger than any elements
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 2, True),
      # Edge case - every occurrence is target
      ([5, 5, 5, 5, 5], 5, 5, True),
      ([5, 5, 5, 5, 5], 5, 3, False),
  ]
  for arr, target, k, want in tests:
    got = solve(arr, target, k)
    assert got == want, f"\ntarget_count_divisible_by_k({arr}, {target}, {k}): got: {got}, want: {want}\n"

if __name__ =='__main__':
    run_tests()


    
        
