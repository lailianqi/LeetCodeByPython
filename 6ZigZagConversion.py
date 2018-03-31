

class Solution:
    # https://leetcode.com/problems/zigzag-conversion/discuss/3403/Easy-to-understand-Java-solution
    # https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = ['']*numRows
        index, step = 0, 1
        for x in s:
            res[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(res)


class Solution_0:
    # https://leetcode.com/problems/zigzag-conversion/discuss/3403/Easy-to-understand-Java-solution
    # https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = ['']*numRows
        i = 0
        while i < len(s):
            j = 0
            while j < numRows and i < len(s):
                res[j] += s[i]
                i, j = i+1, j+1
            j -= 2
            while j >= 1 and i < len(s):
                res[j] += s[i]
                i, j = i+1, j-1
        return ''.join(res)

# l = ['1','3','4','5','6']
# print(''.join(l))
