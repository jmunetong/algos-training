def interval_intersection(arr1, arr2):
    i, j= 0,0
    n1, n2 = len(arr1), len(arr2)
    intervals = []
    while i < n1 and j < n2:
        int1, int2= arr1[i], arr2[j]
        if int1[-1] < int2[0]:
            i +=1
        elif int2[-1] < int1[0]:
            j+=1
        else:
            intervals.append([max(int1[0], int2[0]), min(int1[-1], int2[-1])])
            if int1[-1] < int2[-1]:
                i+=1
            else:
                j +=1
    return intervals
           

    

    # k = 0
    # intervals = [] 
    # for a1 in arr1:
    #     for i in range(k, len(arr2)):
    #         if a1[-1]< arr2[i][0]:
    #             break
    #         if a1[0] > arr2[i][-1]:
    #             continue
    #         else:
    #             intervals.append([max(a1[0], arr2[i][0]), min(a1[-1], arr2[i][-1])])

    # return intervals

            
def run_tests():
  tests = [
      # Example 1 from the book
      ([[0, 1], [4, 6], [7, 8]], [[2, 3], [5, 9], [10, 11]], [[5, 6], [7, 8]]),
      # Example 2 from the book
      ([[2, 4], [5, 8]], [[3, 3], [4, 7]], [[3, 3], [4, 4], [5, 7]]),
      # Additional test cases
      ([], [], []),
      ([[1, 2]], [], []),
      ([[1, 3]], [[2, 4]], [[2, 3]]),
      ([[1, 5]], [[2, 3]], [[2, 3]]),
      ([[1, 2], [3, 4]], [[2, 3]], [[2, 2], [3, 3]]),
  ]
  for arr1, arr2, want in tests:
    got = interval_intersection(arr1, arr2)
    assert got == want, f"\ninterval_intersection({arr1}, {arr2}): got: {got}, want: {want}\n"
    
if __name__ == '__main__':
    run_tests()