import random
def partition(arr):
    low = 0
    high = len(arr) - 1
    mid = low + (high - low +1 )//2
    
    pivot_idx = random.int(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]



def _task(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1

    if high - low <=1:
        return arr
    pivot = arr[low]
    k = high
    i = low
    while True:
        while arr[i] <= pivot and i <k:
            i +=1

        while arr[k] > pivot:
            k -=1
        
        if i >= k:
            break
        arr[i], arr[k] =arr[k], arr[i]

    if arr[k] < arr[low]:
        arr[k], arr[low] = arr[low], arr[k]

    i = low
    j = k
    while True:
        while arr[i] < pivot and i <j:
            i +=1
        
        while arr[j] == pivot and i<=j:
            j -=1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        
    left_high = i
    right_low = k


    return arr, k, left_high, right_low


def run_test():
    samples = [[2, 2, 4, 5, 3,-1,0,2 ], [0,0,0,0,0], [0,-1,1,0,0], [], [2,1,3,2 ]]
    for s in samples:
        print(_task(s))


if __name__ == '__main__':
    run_test()
        