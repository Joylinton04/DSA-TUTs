from collections import Counter
class Solution:
    def isAnagram(self, s:str,t:str):

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def isAnagram2(self, s:str, t:str):
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram2("anagram", "nagaram"))