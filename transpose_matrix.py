"""
Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]] 

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""

def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    return [[j[i] for j in A] for i in range(len(A[0]))]
A = [[1,2,3],[4,5,6]]
print(transpose(self, A))


