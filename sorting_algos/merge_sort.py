
def merge_sort(s):
    """
    Merge sort algorithm
    -----------------

    Time Complexity:
        - O(nlogn): logn the size of the tree (meaning the levels), o(n) equivalent
        to the merging step

    Space complexity:
        - O(n): for creating the supporing arrays during merging
        and along with the recursive stack
    
    
    """

    n = len(s)
    if n < 2:
        return s
    
    half_index = n // 2
    s1 = s[:half_index]
    s2 = s[half_index:]
    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)

def merge(s1, s2, s):
    i, j = 0, 0

    n_final = len(s) 

    while i + j < n_final:

        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j+=1

if __name__ == '__main__':
    arr = [8,5,2,9,5,6,3]
    out = [2,3,5,5,6,8,9]
    merge_sort(arr)
    print(arr)
