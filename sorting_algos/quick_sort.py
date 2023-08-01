"Python file containing quick-sort algorithm implementation"

def quick_sort(arr, i, j):
    """
    Quick sort algorithm

    Params:
    ------
    arr (list array): array to be sorted
    i (int): initial index
    j (int): last index

    Returns:
        list: sorted array

    ----------
    Time Complexity:
        - Worst Case: O(n^2)
        - Average Case: O(n logn)
    
    Space Complexity:
        - O(logn)


     
    """
   
    if i >= j:
        return arr
    
    p_index = j
    p = arr[j]
    j = j - 1

    while i <= j:

        while i <= j and arr[i] < p :
            i += 1

        while  i<=j and p < arr[j]: 
            j -= 1

        if i <=j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    arr[p_index], arr[i] = arr[i], arr[p_index]        
    quick_sort(arr, 0, i-1)
    quick_sort(arr, i+1, p_index)


if __name__ == '__main__':
    arr = [8,5,2,9,5,6,3]
    out = [2,3,5,5,6,8,9]
    quick_sort(i=0, j=len(arr)-1, arr=arr)
    print(arr)

