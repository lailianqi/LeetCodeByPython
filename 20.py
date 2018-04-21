class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        自己的python的解法
        leetcode上面类似的答案
        https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
        """
        dirs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for e in s:
            if e in dirs.keys():
                stack.append(e)
            else:
                if stack and dirs[stack[-1]] == e:
                    stack.pop()
                else:
                    return False
        return not stack
