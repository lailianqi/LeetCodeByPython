class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution
        """
        dir = {'I': 1,   'V': 5,   'X': 10,  'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)-1):
            if dir[s[i]] < dir[s[i+1]]:
                res -= dir[s[i]]
            else:
                res += dir[s[i]]
        return res + dir[s[-1]]
