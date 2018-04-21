class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution
        """
        result = []
        s = ""

        def helper(s, left, right, n):
            if len(s) == 2*n:
                result.append(s)
                return
            if left < n:
                helper(s+'(', left+1, right, n)
            if right < left:
                helper(s+')', left, right+1, n)
        helper(s, 0, 0, n)
        return result


class Solution_0:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
        """

        def generate(p, left, right, parens=[]):
            if left:
                generate(p+'(', left-1, right)
            if left < right:
                generate(p+')', left, right-1)
            if not right:
                parens += p
            return parens
        return generate('', n, n)


class Solution_1:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python?page=1
        """
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right):
                    yield q
                for q in generate(p + ')', left, right-1):
                    yield q
        return list(generate('', n, n))


class Solution_2:
    def generateParenthesis(self, n, open=0):
        """
        :type n: int
        :rtype: List[str]
        https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python?page=1
        """
        if n > 0 <= open:
            return ['('+p for p in self.generateParenthesis(n-1, open+1)] + \
                [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)
