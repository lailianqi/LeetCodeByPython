
# Definition for singly-linked list.

# https://leetcode.com/problems/add-two-numbers/discuss/1032/Python-concise-solution.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur, p, q = result, l1, l2
        carry = 0
        while p or q or carry:
            carry += (p.val if p else 0) + (q.val if q else 0)
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
            p = p.next if p else p
            q = q.next if q else q
        return result.next


a = [1, 2]
b = [1, 3, 4]
c = a, b
for i in c:
    print(sum(i))
print(c)
