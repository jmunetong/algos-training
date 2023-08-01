def bubble_sort(arr):

    """
    Time complexity:
        O(n^2)
    
    Space Complexity:
        o(1)
    """

    for i, _ in enumerate(range(len(arr))):
        for j in range(len(arr) -1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [8,5,2,9,5,6,3]
    out = [2,3,5,5,6,8,9]
    bubble_sort(arr)
    print(arr)