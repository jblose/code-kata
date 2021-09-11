class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        fullLen = len(s)
        dict = {}
        for x in s:
            foundStr = x[: s.find(x + 1)]
            dict[x] = foundStr


s = "abcabcbb"
Solution.lengthOfLongestSubstring(Solution(), s)
