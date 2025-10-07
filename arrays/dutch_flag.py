
import random 

dict_val = {"R":0,
            "W":1,
            "B":2}
def value(s):
    return  dict_val[s]


def sort_colors(arr):
    quick_sort(arr)
    return arr
    

def quick_sort(arr, low=0,high=None):
 
    high = len(arr)-1 if high is None else high
   
    if high <= low:
        return arr
    
    t = random.randint(low, high)
    arr[high], arr[t] = arr[t], arr[high]
    p = _partition(arr, low, high)
    quick_sort(arr, low, p-1)
    quick_sort(arr, p+1, high)
    return arr


def _partition(arr, low, high):
    
    i = low-1
    pivot=value(arr[high])
    for j in range(low, high):
        if value(arr[j]) <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]

    i+=1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def run_tests():
  tests = [
      # Example from the book
      (list("RWBBWRW"), list("RRWWWBB")),
      # Additional test cases
      ([], []),
      (list("R"), list("R")),
      (list("W"), list("W")),
      (list("B"), list("B")),
      (list("RW"), list("RW")),
      (list("WR"), list("RW")),
      (list("RWB"), list("RWB")),
      (list("RRRWWBBB"), list("RRRWWBBB")),
      (list("BBBWWRRR"), list("RRRWWBBB")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since function modifies in place
    sort_colors(arr_copy)
    assert arr_copy == want, f"\nsort_colors({arr}): got: {arr_copy}, want: {want}\n"
    

if __name__ == '__main__':
    run_tests()