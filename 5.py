

class Solution:
    # https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            temp = self.isPalindromicSubstring(s, i, i)
            if len(res) < len(temp):
                res = temp
            temp = self.isPalindromicSubstring(s, i, i+1)
            if len(res) < len(temp):
                res = temp
        return res

    def isPalindromicSubstring(self, s, i, j):
        m = len(s)
        while i >= 0 and j <= m-1 and s[i] == s[j]:
            i, j = i-1, j+1
        return s[i+1:j]
