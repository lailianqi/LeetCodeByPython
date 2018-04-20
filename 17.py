from functools import reduce


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8064/My-java-solution-with-FIFO-queue
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8097/My-iterative-sollution-very-simple-under-15-lines
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8070/One-line-python-solution
        http://www.runoob.com/python/python-func-reduce.html
        """
        dir = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        queue = [''] if digits else []
        for digit in digits:
            current_list = []
            for letter in dir[digit]:
                for combination in queue:
                    current_list.append(combination + letter)
            queue = current_list
        return queue


class Solution_0:
    '''
    https://blog.csdn.net/caimouse/article/details/78129956
    '''

    def letterCombinations(self, digits):
        if '' == digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


class Solution_1:
    '''
    https://blog.csdn.net/caimouse/article/details/78129956
    '''

    def letterCombinations(self, digits):
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        return [a+b for a in self.letterCombinations(digits[:-1])
                for b in self.letterCombinations(digits[-1])] or list(map[digits])

# result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# print(result)

# l = ['13','55']
# print(l+['a'])
