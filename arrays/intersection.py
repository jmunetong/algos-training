def common_elements(arr1, arr2):
  
    i=0
    j=0
    n1 = len(arr1)
    n2 = len(arr2)
    final_arr = []
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            final_arr.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j+=1
             
    return final_arr


        



def run_tests():
    tests = [
        # Example 1 from the book
        ([1, 2, 3], [1, 3, 5], [1, 3]),
        # Example 2 from the book
        ([1, 1, 1], [1, 1], [1, 1]),
        # Additional test cases
        ([], [], []),
        ([1], [], []),
        ([], [1], []),
        ([1], [1], [1]),
        ([1, 2, 3], [4, 5, 6], []),
        ([1, 2, 2, 3], [2, 2, 3], [2, 2, 3]),
    ]
    for arr1, arr2, want in tests:
            got = common_elements(arr1, arr2)
            assert got == want, f"\ncommon_elements({arr1}, {arr2}): got: {got}, want: {want}\n"


if __name__ == '__main__':
    run_tests()