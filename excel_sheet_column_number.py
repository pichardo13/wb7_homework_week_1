"""
Leetcode url: https://leetcode.com/problems/excel-sheet-column-number/
Given a column title as appear in an Excel sheet, return its corresponding column number.

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""

def titleToNumber(str):
    total = 0
    for i in range(len(str)):
        total += pow(26, len(str) - i - 1) * (ord(str[i]) - ord('A') + 1)
    return total

input_1 = "A"
print(titleToNumber(input_1))

input_2 = 'AB'
print(titleToNumber(input_2))

input_3 = 'ZY'
print(titleToNumber(input_3))