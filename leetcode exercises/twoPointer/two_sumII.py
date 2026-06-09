class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        index2 = len(numbers) - 1
        
        while index < index2:
            total = numbers[index] + numbers[index2]
            if total == target:
                return [index+1, index2+1]
            
            if total < target:
                index += 1
            else:
                index2 -= 1
            
        return [-1,-1]


sol = Solution()
numbers = [2,3,4]
print(sol.twoSum(numbers, 6))