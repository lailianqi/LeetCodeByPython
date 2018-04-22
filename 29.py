class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        来自LeetCode的解法
        https://leetcode.com/problems/divide-two-integers/discuss/13407/Detailed-Explained-8ms-C++-solution
        https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, mul = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                mul <<= 1
            dividend -= temp
            res += mul
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
