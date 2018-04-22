# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        自己的第一种解法
        """
        result = ListNode(0)
        current, newCurrent = head, result
        while current and current.next:
            temp = current.next.next
            newCurrent.next = current.next
            newCurrent = newCurrent.next
            newCurrent.next = current
            newCurrent = newCurrent.next
            current = temp
        newCurrent.next = current
        return result.next


class Solution_0:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        来自LeetCode递归的写法
        https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11030/My-accepted-java-code.-used-recursion.
        """
        if head == None or head.next == None:
            return head
        cur = head.next
        head.next = self.swapPairs(cur.next)
        cur.next = head
        return cur
