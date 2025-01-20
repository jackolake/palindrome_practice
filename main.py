"""
125. Valid Palindrome

Given a string text, return true if it is a palindrome, or false otherwise.

For this question, letters are NOT case-sensitive, for example, "LEVeL" is a palindrome.
"""
# Change this function so it works correctly
import re
def is_palindrome(text):
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return clean_text == clean_text[::-1]


if __name__ == '__main__':
    test_cases = [('level', True),
                  ('LEVeL', True),
                  ('levy', False),
                  ('rotor', True),
                  ('motor', False),
                  ('No lemon no melon', True),
                  ('No No', False),
                  ('2025202', True),
                  ('100P', False),
                  ('Do geese see God', True)]
    for test_text, expected in test_cases:
        result = is_palindrome(test_text)
        msg = 'Correct' if expected == result else 'Wrong'
        print(f'[{msg:7s}] is_palindrome("{test_text}") should be {expected}')
