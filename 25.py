class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        自己对LeetCode的完美的改写 成功ac
        https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11423/Short-but-recursive-Java-code-with-comments
        """
        dummy = ListNode(0)
        current, dummy.next = head, head
        length = 0
        while current:
            current = current.next
            length += 1
        preHead, current = dummy, head
        while length >= k:
            newTail = current
            for _ in range(0, k):
                temp = current.next
                current.next = preHead.next
                preHead.next = current
                current = temp
            preHead = newTail
            length -= k
        preHead.next = current
        return dummy.next
