"""
https://leetcode.com/problems/number-complement/

Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

"""
Step 1: Convert number into bits

Step 2: Find the length of the bits 

Step 3: Find number that corresponds to the length from step 2 with all 1's

Step 4: Using bit from step 3, compare this to the number given using XOR
"""

def findComplement(num):
    #step 1
    bits = bin(num) #this will return binary number of the form: 0bxxxx

    #step 2
    l = len(bits) - 2 #we only want the bit length, subtract 2 bc of the '0b'

    #step 3
    num2 = (2 ** l) - 1 #number of length l with bits all 1

    return num ^ num2 #XOR 

print(findComplement(5))
print(findComplement(10))
