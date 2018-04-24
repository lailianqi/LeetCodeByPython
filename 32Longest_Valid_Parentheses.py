class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        来自LeetCode的答案 写的非常的好
        https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack
        """
        stack, res, s = [0], 0, ')'+s
        for i in range(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res


class Solution_1:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        上面的改进版
        https://leetcode.com/problems/longest-valid-parentheses/discuss/14167/Simple-JAVA-solution-O(n)-time-one-stack
        """
        stack, res = [-1], 0
        for i in range(0, len(s)):
            if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res


class Solution_2:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        dp的写法  解法来自LeetCode
        https://leetcode.com/problems/longest-valid-parentheses/discuss/14133/My-DP-O(n)-solution-without-using-stack
        """
        dp, s = [0], ')'+s
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - dp[-1] - 1] == '(':
                dp.append(dp[-1] + 2 + dp[-2-dp[-1]])
            else:
                dp.append(0)
        return max(dp)
