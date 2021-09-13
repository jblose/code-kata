class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        fullLen = len(s)
        dict = {}
        for x, alpha in enumerate(s):
            if x < fullLen:
                foundAlpha = s.find(alpha, x + 1)
                foundStr = s[x:foundAlpha]
                repeats = False
                for y in foundStr:
                    if foundStr.count(y) > 1:
                        repeats = True
                if repeats == False:
                    print(foundStr)
                    dict[x] = foundStr


s = "abcabcbb"
Solution.lengthOfLongestSubstring(Solution(), s)
