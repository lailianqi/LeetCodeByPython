class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        好题 很典型的dp的问题
        这里的第一种方案超时
        """
        m = len(nums)
        dp = [-1]*m
        dp[0] = 0
        for i in range(1, m):
            for j in range(i):
                if dp[j] != -1 and j+nums[j] >= i:
                    dp[i] = min(dp[j]+1, dp[i]) if dp[i] != -1 else dp[j]+1
        return dp[m-1]


class Solution_0:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这里借鉴了miss的思想[left,right] 也是以前c++版本里面的bfs的解法
        来源于LeetCode的答案
        https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
        https://leetcode.com/problems/jump-game-ii/discuss/18019/10-lines-C++-(16ms)-Python-BFS-Solutions-with-Explanations
        """
        miss, m, res, curEnd = 0, len(nums), 0, 0
        for i in range(m-1):
            miss = max(miss, i+nums[i])
            if i == curEnd:
                res += 1
                curEnd = miss
                if curEnd >= m-1:
                    break
        return res


class Solution_1:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        上面的另外的一种写法
        """
        miss, m, res, curEnd = 0, len(nums), 0, 0
        for i in range(m-1):
            miss = max(miss, i+nums[i])
            if miss >= m-1:
                return res+1
            if i == curEnd:
                res += 1
                curEnd = miss
        return res
