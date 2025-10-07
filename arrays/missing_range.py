def missing_numbers_range(arr, low, high):

    i = 0
    next_val = low
    N = len(arr)-1
    final_arr = []
    while i < N:
        current = arr[i]
        if current <= low:
            i +=1
        
        