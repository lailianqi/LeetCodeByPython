

class Solution:
    '''
    # 自己的第一种解法
    # 类似的答案的链接
    # https://leetcode.com/problems/palindrome-number/discuss/5128/Python-solution-based-on-the-algorithm-in-leetcode-blog
    '''

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]
