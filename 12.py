

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.
        """
        a = [1000, 900, 500, 400, 100, 90, 50,
             40,   10,  9,   5,   4,   1]
        b = ["M",  "CM", "D",  "CD", "C",  "XC", "L",
             "XL", "X",  "IX", "V",  "IV", "I"]
        i = 0
        res = ""
        while num != 0:
            while num >= a[i]:
                num -= a[i]
                res += b[i]
            i += 1
        return res


class Solution_0:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        https://leetcode.com/problems/integer-to-roman/discuss/6273/Share-My-Python-Solution-96ms
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num/1000] + C[(num % 1000)/100] + X[(num % 100)/10] + I[num % 10]
