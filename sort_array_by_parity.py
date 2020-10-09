class Solution(object):
   #sort array, even numbers in the front and odd in the end
   #sort even and odd in ascending order
   def sortArrayByParity(self, A):
        #create even and odd array and store respective numbers into array
        even = []
        odd = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        #sort elements in array
        even.sort()
        odd.sort()
        return even + odd #combine lists 

sol = Solution()
print(sol.sortArrayByParity([10,3,2,6,9,22,14,13]))