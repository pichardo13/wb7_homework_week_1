"""
Increment the number by 1, the number will be represented as an array of digits

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    numString = ''.join(map(str, digits))
    number = int(numString) + 1
    return [int(i) for i in str(number)]

print([1,0] == plusOne([9]))
print(plusOne([1,9,0]))



