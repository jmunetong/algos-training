# Write a method to replace all spaces ina string with '%20' You may assume that the string has sufficient space at the end to hold additional characters,
# and that you are given the "true" length of the string. 

def urlify(str1):
    str1 = "%20".join(str1.strip().split(" "))
    return str1


def test_urlify():
    test_cases = [
        ("Mr John Smith    ", "Mr%20John%20Smith"),  # Given example
        ("Hello World  ", "Hello%20World"),  # One space replacement
        ("Python is fun  ", "Python%20is%20fun"),  # Multiple spaces
        ("NoSpaces", "NoSpaces"),  # No spaces in string
        (" ", "%20"),  # Single space
        ("   ", "%20%20%20"),  # Multiple spaces only
        ("  LeadingSpace", "%20%20LeadingSpace"),  # Leading spaces
        ("TrailingSpace  ", "TrailingSpace%20%20"),  # Trailing spaces
        ("  Multiple   Spaces   ", "%20%20Multiple%20%20%20Spaces%20%20%20"),  # Consecutive spaces
        ("", ""),  # Empty string case
        ("Special !@# $%^&*()  ", "Special%20!@#%20$%^&*()")  # Spaces between special characters
    ]
    
    for i, (input_str, expected_output) in enumerate(test_cases):
        result = urlify(input_str)
        if result != expected_output:
            print(f"Test case {i+1} failed:")
            print(f"  Input: '{input_str}'")
            print(f"  Expected: '{expected_output}'")
            print(f"  Got: '{result}'\n")
        else:
            print(f"Test case {i+1} passed!")

# Run the tests
test_urlify()