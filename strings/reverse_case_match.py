def reverse_case_match(s):
    N = len(s)
    l = 0
    h = N-1

    while l < N and h >=0:
        if s[l].isupper():
            l +=1
            continue
        
        if s[h].islower():
            h -=1
            continue

        if s[l] != s[h].lower():
            return False

        l +=1
        h -=1


    return True


def run_tests():
  tests = [
      # Example 1 from the book
      ("haDrRAHd", True),
      # Example 2 from the book
      ("haHrARDd", False),
      # Additional test cases
      ("", True),
      ("aA", True),
      ("Aa", True),
      ("BbbB", True),
      ("abAB", False),
      ("abBA", True),
      ("helloworldHELLOWORLD", False),
  ]
  for s, want in tests:
    got = reverse_case_match(s)
    assert got == want, f"\nreverse_case_match({s}): got: {got}, want: {want}\n"


if __name__ == '__main__':
   run_tests()