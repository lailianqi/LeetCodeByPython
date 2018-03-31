class Solution:
    # https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if(len(str) == 0):
            return 0
        ls = list(str.strip())
        sign = (-1, 1)[ls[0] != '-']
        res, i = 0, 0
        i = i+1 if ls[0] in ('-', '+') else i
        while i < len(ls) and ls[i].isdigit():
            res = res*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res, 2**31-1))


s = Solution()
s.myAtoi("1")
