import queue
from heapq import heappush, heappop, heapreplace, heapify
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    自己的按照原来的c++代码写的版本
    '''

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if (len(lists) == 0):
            return None
        return self.mergeSort(lists, 0, len(lists)-1)

    def mergeSort(self, lists, left, right):
        if left < right:
            mid = (left + right)//2
            l1 = self.mergeSort(lists, left, mid)
            l2 = self.mergeSort(lists, mid + 1, right)
            return self.mergeTwoLists(l1, l2)
        return lists[left]

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        合并两个链表的函数
        """
        result = ListNode(0)
        current = result
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return result.next


class Solution_0:
    '''
    优先队列的写法 来自LeetCode 
    而且这破代码无法在python3下运行
    https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
    '''

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        q = queue.PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            current.next = q.get()[1]
            current = current.next
            if current.next:
                q.put((current.next.val, current.next))
        return dummy.next


class Solution_1:
    '''
    优先队列的写法 来自LeetCode 这个解法非常的不错
    https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
    '''

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = current = ListNode(0)
        listsNode = [(e.val, e) for e in lists if e]
        heapify(listsNode)
        while listsNode:
            val, node = listsNode[0]
            if node.next is None:
                heappop(listsNode)
            else:
                heapreplace(listsNode, (node.next.val, node.next))
            current.next = node
            current = current.next
        return dummy.next
