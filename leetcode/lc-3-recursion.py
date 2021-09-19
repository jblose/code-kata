class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        if Solution.isUnique(s):
                return len(s)
        return Solution.longestSub(s,longest)

        # fullLen = len(s)
        # if fullLen == 1:
        #     return 1
        # longest = 0
        # for x, alpha in enumerate(s):
        #     if x < fullLen:
        #         foundAlpha = s.find(alpha, x + 1)
        #         foundStr = s[x:foundAlpha]
        #         repeats = False
        #         for y in foundStr:
        #             if foundStr.count(y) > 1:
        #                 repeats = True
        #         if repeats == False and len(foundStr) > longest:
        #             longest = len(foundStr)
        # return longest

    def isUnique(s):
        if len(s) == 0:
            return True
        elif s[1:].find(s[0:1]) < 0 :
            return Solution.isUnique(s[1:])
        else:
            return False

    def longestSub(s, longest):
        if len(s) == 0:
            return longest
        else:
            alpha = s[0:1]
            templong = s[1:].find(alpha) + 1
            if templong > longest:
                longest = templong
            return Solution.longestSub(s[1:],longest)
        
        return longest

def test_abcabcbb():
    assert Solution.lengthOfLongestSubstring(Solution(), "abcabcbb") == 3


def test_bbbbb():
    assert Solution.lengthOfLongestSubstring(Solution(), "bbbbb") == 1


def test_pwwkew():
    assert Solution.lengthOfLongestSubstring(Solution(), "pwwkew") == 3

def test_emtpy():
    assert Solution.lengthOfLongestSubstring(Solution(), "") == 0

def test_blank():
    assert Solution.lengthOfLongestSubstring(Solution(), " ") == 1

def test_au():
    assert Solution.lengthOfLongestSubstring(Solution(), "au") == 2


Solution.lengthOfLongestSubstring(Solution(), "pwwkew")