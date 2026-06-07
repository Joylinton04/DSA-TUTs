from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
       m = defaultdict(list)
       for word in strs:
            sorted_word = ''.join(sorted(word))
            m[sorted_word].append(word)

       res = []
       for k in m:
            res.append(m[k])
       return res




sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))