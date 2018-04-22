class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        暴力的解法可解
        https://leetcode.com/problems/implement-strstr/discuss/12811/Share-my-accepted-java-solution
        https://leetcode.com/problems/implement-strstr/discuss/12814/My-answer-by-Python
        """
        m = len(haystack) - len(needle)
        for i in range(m+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
