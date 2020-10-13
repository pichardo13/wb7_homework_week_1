"""Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
"""
from string import ascii_lowercase
def isPalindrome(text):
    text = text.lower()
    left = 0
    right = len(text) - 1

    while left < right:
        while text[left] not in ascii_lowercase:
            left += 1
        while text[right] not in ascii_lowercase:
            right -= 1
        if text[left] != text[right]:
            return False
        else:
            right -= 1
            left += 1
    return True

input_1 = "race a car"
print(isPalindrome(input_1))

input_2 = "A man, a plan, a canal: Panama"
print(isPalindrome(input_2))

input_3 = "Racecar"
print(isPalindrome(input_3))
