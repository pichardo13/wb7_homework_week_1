"""
https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1
"""
def singleNumber(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

input_1 = [2,2,1]
print(singleNumber(input_1))

input_2 = [4,2,1,2,1]
print(singleNumber(input_2))