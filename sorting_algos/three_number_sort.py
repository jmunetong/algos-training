def threeNumberSort(array, order):
    # Write your code here.

    f = 0
    s = 0
    t = len(array) - 1

    while s <= t:
        if array[s] == order[1]:
            s += 1
        elif array[s] == order[0]:
            array[s], array[f] =  array[f], array[s]
            s += 1
            f += 1
        else:
            array[t], array[s] = array[s], array[t]
            t -= 1

    return array

if __name__ == "__main__":
    order = [11,7,9]
    array = [9,9,9,7,9,7,9,9,7,9]
    threeNumberSort(array, order)
