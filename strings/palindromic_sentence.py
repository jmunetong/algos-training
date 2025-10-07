

def palindromic_sentence(s):
    l = 0
    h = len(s) -1
    s = s.lower()
    while l < h:
        if not s[l].isalpha():
            l += 1
            continue
        
        if not s[h].isalpha():
            h -=1
            continue

        if s[h] != s[l]:
            return False
        
        l +=1
        h -=1

    return True




    # Solution with nested loops. I am going to try to not use nested loops if possible
    # l = 0
    # h = len(s)-1
    # s = s.lower()

    # while l < h:
    #     while l < h and not s[l].isalpha():
    #         l += 1
        
    #     while l < h and not s[h].isalpha():
    #         h -= 1

    #     if s[l] != s[h]:
    #         return False
    #     l +=1
    #     h -=1
    
    # return True


def run_tests():
    tests = [
        # Example from the book
        ("Bob wondered, 'Now, Bob?'", True),
        # Additional test cases
        ("", True),
        ("a", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("hello", False),
        (".,?!'", True),
    ]
    for s, want in tests:
        got = palindromic_sentence(s)
        assert got == want, f"\npalindromic_sentence({s}): got: {got}, want: {want}\n"

if __name__ == '__main__':
   run_tests()