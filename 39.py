class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        自己的第一种解法 一次ac 这系列的题目应该还是好题
        下面是LeetCode的解法 其实差不多
        https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
        https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c++-solution-use-backtracking-easy-understand.
        https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
        """
        res = []

        def helper(candidates, target, current, currlist, start=0):
            if current > target:
                return
            if current == target:
                res.append(currlist.copy())
            for i in range(start, len(candidates)):
                currlist.append(candidates[i])
                helper(candidates, target, current+candidates[i], currlist, i)
                currlist.pop()
        helper(candidates, target, 0, [], 0)
        return res
