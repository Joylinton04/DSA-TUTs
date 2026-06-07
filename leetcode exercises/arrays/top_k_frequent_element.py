from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        return [item[0] for item in counts.most_common(k)]

sol = Solution()
print(sol.topKFrequent(nums=[1,1,1,2,2,3,3,3,3,3], k=2))