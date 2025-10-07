
def palindrome(s):
    l, h = 0, len(s)-1
    while l < h:
        if s[l] != s[h]:
            return False
        l+=1
        h -=1

    return True


def run_tests():
  tests = [
      # Example from the book
      ("level", True),
      ("naan", True),
      # Additional test cases
      ("", True),
      ("a", True),
      ("ab", False),
      ("abc", False),
      ("abba", True),
      ("abcba", True),
  ]
  for s, want in tests:
    got = palindrome(s)
    assert got == want, f"\npalindrome({s}): got: {got}, want: {want}\n"


if __name__ == "__main__":
    run_tests()