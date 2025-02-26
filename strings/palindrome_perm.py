## Given a string, write a function to check if it is a permutation of a palindrome
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The Palindrome does not need to be 
# limited to just a dictionary of words.
from functools import reduce
def is_palindrome_perm(str):
    str = str.lower()
    str = str.replace(" ", "")
    if str == str[::-1]:
        return True
    else:
        dict_str =  {}
        for letter in str:
            if letter not in dict_str:
                dict_str[letter] = 1
            else:
                dict_str[letter] +=1
        counts = list(map(lambda x: x%2, dict_str.values()))
        if not len(str)%2: # if my length is even
            return not any(counts)
        else:
            total = reduce(lambda x, y: x+y, counts)
            return total ==1



def test_is_palindrome_perm():
    test_cases = [
        ("racecar", True),  # Already a palindrome
        ("carrace", True),  # A permutation of "racecar"
        ("taco cat", True),  # A permutation of "tacocat" (ignoring spaces)
        ("atco cta", True),  # Another permutation of "tacocat"
        ("hello", False),  # Cannot be rearranged into a palindrome
        ("abcd", False),  # All characters appear only once
        ("aabb", True),  # Can be rearranged into "abba"
        ("AaBb", True),  # Case-insensitive check
        ("A Santa at NASA", True),  # Ignores spaces and case
        ("No lemon, no melon", True),  # Ignores spaces and punctuation
        ("", True),  # Empty string is trivially a palindrome
        ("a", True),  # Single character is always a palindrome
        ("aa", True),  # Two of the same character forms a palindrome
        ("abcba", True),  # Odd-length palindrome
        ("abccba", True),  # Even-length palindrome
        ("abcdba", False),  # Odd-length, not a palindrome permutation
        # ("xyzxyz", False),  # Even length but cannot be rearranged into a palindrome
    ]

    for i, (input_str, expected_output) in enumerate(test_cases):
        result = is_palindrome_perm(input_str)
        if result != expected_output:
            print(f"Test case {i+1} failed:")
            print(f"  Input: '{input_str}'")
            print(f"  Expected: {expected_output}")
            print(f"  Got: {result}\n")
        else:
            print(f"Test case {i+1} passed!")

# Run the tests
test_is_palindrome_perm()