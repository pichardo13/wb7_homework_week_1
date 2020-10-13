"""
https://leetcode.com/problems/hamming-distance/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

def hammingDistance(x, y):
    bits = x ^ y #finding differing bits
    count = 0 #will count how many bits are different

    while bits > 0: 
        count += bits & 1 #add to count 1 everytime a bit in 2^0 appears (basically counts 1 bits)
        bits >>= 1 #move bit to the right
    return count

print(hammingDistance(1, 4) == 2)
print(hammingDistance(1, 11) == 2)