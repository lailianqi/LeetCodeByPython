

class Solution:
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1781/Python-solution-with-comments.
    # 我的第一种方法
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, start = 0, 0
        dir = set()
        for i in range(len(s)):
            while s[i] in dir:
                dir.remove(s[start])
                start += 1
            dir.add(s[i])
            result = max(result, len(dir))
        return result


class Solution_0:
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, start = 0, 0
        dir = {}
        for i in range(len(s)):
            if s[i] in dir and start <= dir[s[i]]:
                start = dir[s[i]] + 1
            else:
                result = max(result, i - start + 1)
            dir[s[i]] = i
        return result


class Solution_1:
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1737/C++-code-in-9-lines.
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, start = 0, -1
        dir = {}
        for i in range(len(s)):
            if s[i] in dir and start < dir[s[i]]:
                start = dir[s[i]]
            else:
                result = max(result, i - start)
            dir[s[i]] = i
        return result


s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
