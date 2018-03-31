

class Solution:
    # https://leetcode.com/problems/reverse-integer/discuss/4220/Simple-Python-solution-56ms
    # https://leetcode.com/problems/reverse-integer/discuss/4055/Golfing-in-Python
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def sign(x): return x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1]


# s = -12345
# print (int(str(-s)[::-1]))
