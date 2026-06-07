import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == " ":
            return True

        result = re.sub(r"[^a-zA-z]", "", s).lower()
        left = 0
        right = len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True


        

        

sol = Solution()
mes = "race a car"
print(sol.isPalindrome(mes))