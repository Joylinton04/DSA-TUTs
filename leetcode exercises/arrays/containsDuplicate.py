class Solution:
    def containsDup(self, nums):
        unique = set()
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False

    


solu = Solution()
nums = [1,2,4]
print(solu.containsDup(nums))