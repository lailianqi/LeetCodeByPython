class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        自己的第一种方法

        LeetCode类似的解法
        https://leetcode.com/problems/combination-sum-ii/discuss/16933/My-84ms-python-recursive-solution.
        https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments
        """
        res = []
        candidates.sort()

        def helper(candidates, target, current, currlist, start=0):
            if current > target:
                return
            if current == target:
                res.append(currlist.copy())
            for i in range(start, len(candidates)):
                if i == start or candidates[i] != candidates[i-1]:
                    currlist.append(candidates[i])
                    helper(candidates, target, current +
                           candidates[i], currlist, i+1)
                    currlist.pop()
        helper(candidates, target, 0, [], 0)
        return res


a = [2, 5, 2, 1, 2]
s = Solution()
s.combinationSum2(a, 5)
