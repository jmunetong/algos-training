def quicksort(arr, l, r):

    if l >= r:
        return 
    start = l
    end = r
    p_idx = (l + r)//2
    p = arr[p_idx]
    while l <=r:
        while arr[l] < p:
            l += 1
        while arr[r] > p :
            r -= 1
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l +=1
            r -=1
    quicksort(arr,start, r)
    quicksort(arr, l, end)

