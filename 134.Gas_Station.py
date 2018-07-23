class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, remain_gas, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if remain_gas < 0:
                start = i
                remain_gas = gas[i] - cost[i]
            else:
                remain_gas += gas[i] - cost[i]
        return start if total >= 0 else -1
