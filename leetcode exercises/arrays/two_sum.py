class Solution:
    def twoSum(self, nums, target):
        index = 0
        index2 = 0
        for i in nums:
            for j in nums:
                if (i+j) == target and index != index2:
                    return [index, index2]
                index2 += 1
            index += 1
            index2 = 0
        return []


sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))
