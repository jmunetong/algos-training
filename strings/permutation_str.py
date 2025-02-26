# Given two strings write a method to decide if one is a permutation of the other
def is_perm(str1: str,str2: str)-> bool:
    if len(str1) != len(str2):
        return False
    else:
        s1 = "".join(sorted(str1))
        s2 = "".join(sorted(str2))
        return s1 == s2

# Given two strings write a method to decide if one is a permutation of the other
def is_perm(str1: str,str2: str)-> bool:
    if len(str1) != len(str2):
        return False
    else:
        s1 = "".join(sorted(str1))
        s2 = "".join(sorted(str2))
        return s1 == s2
    
def test_is_perm():
    # Basic test cases
    assert is_perm("abcd", "dcba") == True  # Same letters, different order
    assert is_perm("hello", "oellh") == True  # Same letters, different order
    assert is_perm("abc", "def") == False  # Completely different letters
    assert is_perm("aabb", "bbaa") == True  # Same frequency of letters
    assert is_perm("abc", "abcd") == False  # Different lengths

    # Edge cases
    assert is_perm("", "") == True  # Two empty strings
    assert is_perm("a", "a") == True  # Single character, same
    assert is_perm("a", "b") == False  # Single character, different
    assert is_perm("aaa", "aaa") == True  # Identical strings
    assert is_perm("abc", "ABC") == False  # Case-sensitive (if function is case-sensitive)
    
    # Special character cases
    assert is_perm("a!b@c", "c@b!a") == True  # Permutation with special characters
    assert is_perm("123", "321") == True  # Numbers as characters
    assert is_perm("123", "122") == False  # Different frequency of characters
    assert is_perm("racecar", "carrace") == True  # Palindrome permutation

    print("All test cases passed!")

# Run tests
test_is_perm()