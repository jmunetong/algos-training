def partition(arr, pivot):
    left = 0
    right = len(arr)-1
    N = len(arr)
    while left < right:
        if arr[left] <= pivot:
            left +=1
        elif arr[right] > pivot:
            right -=1
        else:
           arr[left], arr[right] = arr[right], arr[left]
           left +=1
           right -= left

        # let us find the boundary:
        t = 0
        while t < N:
           if arr[t] == pivot:
              break
           t +=1

        k = t +1
        while k < N:
            if arr[k] < arr[t]:
                arr[k], arr[t] = arr[t], arr[k]
                t +=1

            k+=1
        
    return arr

def run_tests():
  def is_valid_partition(arr, pivot):
    # Find boundaries between sections
    first = 0
    while first < len(arr) and arr[first] < pivot:
      first += 1
    second = first
    while second < len(arr) and arr[second] == pivot:
      second += 1

    # Check that all elements are in their correct sections
    for i in range(first):
      if arr[i] >= pivot:
        return False
    for i in range(first, second):
      if arr[i] != pivot:
        return False
    for i in range(second, len(arr)):
      if arr[i] <= pivot:
        return False
    return True

  tests = [
      # Example 1 from the book
      ([1, 7, 2, 3, 3, 5, 3], 4),
      # Example 2 from the book
      ([1, 7, 2, 3, 3, 5, 3], 3),
      # Additional test cases
      ([], 1),
      ([1], 1),
      ([1, 2], 1),
      ([2, 1], 1),
      ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4),
      ([9, 3, 7, 6, 2, 8], 6)
  ]
  for arr, pivot in tests:
    arr_copy = arr.copy()  # Make a copy since partition modifies in place
    partition(arr_copy, pivot)
    assert is_valid_partition(arr_copy, pivot), \
        f"\npartition({arr}, {pivot}): got: {arr_copy}\n"
    
if __name__ == '__main__':
   run_tests()