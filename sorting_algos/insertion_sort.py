def insertion_sort(arr):
    
    """
    Time complexity o(n^2) because of the two for looops 
    Space complexity o(1)

    
    """
    for i in range(len(arr)):
        if i > 0:
            m = i
            for j in reversed(range(0, i)):
                if arr[m] < arr[j]:
                    arr[m], arr[j] = arr[j], arr[m]
                    m = j 

    return arr


if __name__ == '__main__':
    arr = [8,5,2,9,5,6,3]
    out = [2,3,5,5,6,8,9]
    insertion_sort(arr)
    print(arr)




                