def shift(arr, word):

    i = 0 # array index
    j = 0 # word index
    n_w = len(word)
    n_a = len(arr)
    word = list(word)
    k =0
    while i < n_a and j < n_w:
        if arr[i] != word[j]:
            arr[k] = arr[i]
            k +=1
        else:
            j +=1
        i +=1

    while i < n_a:
       arr[k] = arr[i]
       k+=1
       i+=1

    m = n_a - n_w
    j = 0
    while m < n_a:
       arr[m] = word[j]
       j +=1
       m +=1

    return arr 
       


       


def run_tests():
  tests = [
      # Example 1 from the book
      (list("seekerandwriter"), "edit", list("sekeranwreredit")),
    #   Example 2 from the book
      (list("bacb"), "ab", list("bcab")),
      # Example 3 from the book
      (list("babc"), "b", list("abcb")),
      # Additional test cases
      ([], "", []),
      (list("a"), "a", list("a")),
      (list("abc"), "", list("abc")),
      (list("hello"), "ho", list("ellho")),
      (list("abcabc"), "abc", list("abcabc")),
  ]
  for arr, word, want in tests:
    arr_copy = arr.copy()  # Make a copy since move_word modifies in place
    print(arr)
    arr_copy = shift(arr_copy, word)
    assert arr_copy == want, f"\nmove_word({arr}, {word}): got: {arr_copy}, want: {want}\n"

run_tests()