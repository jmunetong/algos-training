def sort_valley_array(arr):
    N = len(arr)
    l, h  = 0, N-1
    new_arr = []
    if len(arr) == 0:
        return new_arr
    if len(arr) == 1:
        return arr
    while True:
        l+=1 
        if l >= h or arr[l] > arr[l-1]:
            l -=1
            break
        
    
    while True:
        h -=1
        if h<=l or arr[h] <= arr[h-1]:
            h +=1
            break   
      
    
    while l >=0  and h < N:
       
        if arr[l] <= arr[h]:
            new_arr.append(arr[l])
            l -=1
        else:
            new_arr.append(arr[h])
            h +=1
    
 
    while l >=0:
     
        new_arr.append(arr[l])
        l -=1
    
    while h < N:
        new_arr.append(arr[h])
        h +=1

    return new_arr


def run_tests():
  tests = [
      # Example 1 from the book
      ([8, 4, 2, 6], [2, 4, 6, 8]),
      # Example 2 from the book
      ([1, 2], [1, 2]),
      # Example 3 from the book
      ([2, 2, 1, 1], [1, 1, 2, 2]),
      # Additional test cases
      ([], []),
      ([1], [1]),
      ([3, 2, 1, 4], [1, 2, 3, 4]),
      ([5, 4, 3, 2, 1, 2, 3], [1, 2, 2, 3, 3, 4, 5]),
      ([1, 1, 1, 1], [1, 1, 1, 1]),
  ]
  for arr, want in tests:
    got = sort_valley_array(arr)
    assert got == want, f"\nsort_valley_array({arr}): got: {got}, want: {want}\n"

if __name__ == '__main__':
    run_tests()