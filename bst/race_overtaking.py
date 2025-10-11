def solve(p1, p2):
    n = len(p1)
    assert len(p1) == len(p2), "The input given is incorrect"
    i = 0
    j = n -1
    result = n -1
    while i <=j:
        mid = i + (j - i) //2
        if p1[mid] > p2[mid]:
            i = mid + 1
        else:
            result= mid
            j = mid - 1

    return result

def run_tests():
  tests = [
      # Example 1 from book
      ([2, 4, 6, 8, 10], [1, 3, 5, 9, 11], 3),
      # Example
      ([2, 3, 4, 5, 6], [1, 2, 3, 6, 7], 3),
      # Example
      ([3, 4, 5], [2, 5, 6], 1),
      # Edge case - overtake at start
      ([2, 3], [1, 4], 1),
  ]

  for p1, p2, want in tests:
    got =solve(p1, p2)
    assert got == want, f"\nrace_overtaking({p1}, {p2}): got: {got}, want: {want}\n"

if __name__ == '__main__':
   run_tests()