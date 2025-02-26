# Determine whether a string has all unique characters
# Note that this is not an optimal solution.
def is_unique_suboptimal(str_sample):
    str_sample = "".join(sorted(str_sample)) # This will run in O(nlogn)
    n = len(str_sample)
    for idx in range(1, n):
        if str_sample[idx-1] == str_sample[idx]:
            return False
    return True

# Consider the case where we are able to use
def is_unique(str_sample):
    return len(str_sample) == len(set(str_sample))


if __name__ == '__main__':
    str1 = 'aaaab'
    assert not is_unique(str1)
    str2 = 'una de las casas'
    assert not is_unique(str2)
    str3= 'mother'
    assert  is_unique(str3)
