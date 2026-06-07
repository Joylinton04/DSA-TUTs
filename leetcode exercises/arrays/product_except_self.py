class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n
        
        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Calculate the final answer
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]
            
        return answer
            
        



sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))