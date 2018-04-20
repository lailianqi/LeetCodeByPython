# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        自己的python没添加额外节点的方法
        """
        current_slow = head
        current_faster = head
        prev = None
        for _ in range(n):
            current_faster = current_faster.next
        while current_faster != None:
            prev = current_slow
            current_slow = current_slow.next
            current_faster = current_faster.next
        if prev == None:
            head = current_slow.next
        else:
            prev.next = current_slow.next
        return head


class Solution_0:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        自己的python添加额外节点的方法
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8804/Simple-Java-solution-in-one-pass
        """
        result = ListNode(0)
        result.next = head
        current_slow, current_faster, prev = head, head, result
        for _ in range(n):
            current_faster = current_faster.next
        while current_faster != None:
            prev = current_slow
            current_slow = current_slow.next
            current_faster = current_faster.next
        prev.next = current_slow.next
        return result.next


class Solution_1:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        leetcode写的不错的解法
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
