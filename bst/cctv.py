
def solve(t1, t2, is_stolen):   

    if is_stolen(t1):
        return t1

    if not is_stolen(t2-1):
        return t2

    while t2 - t1> 1:
        mid = t1 + (t2 - t1)//2
        if is_stolen(mid):
            t2 = mid
        else:
            t1 = mid


    return t2       



def run_tests():
  tests = [
      # Example 1 - stolen at t=5
      (1, 10, lambda t: t >= 5, 5),
      # Example 2 - stolen at start
      (1, 5, lambda t: t >= 2, 2),
      # Example 3 - stolen at end
      (1, 5, lambda t: t >= 5, 5),
      # Edge case - two timestamps
      (5, 6, lambda t: t >= 6, 6)
  ]

  for t1, t2, is_stolen, want in tests:
    got = solve(t1, t2, is_stolen)
    assert got == want, f"\nfind_bike({t1}, {t2}): got: {got}, want: {want}\n"


if __name__=='__main__':
   run_tests()