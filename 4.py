class Solution:
    # https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m+n))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.getKth(nums1, nums2, length // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, length // 2) + self.getKth(nums1, nums2, length // 2 + 1)) / 2

    def getKth(self, a, b, k):
        m, n = len(a), len(b)
        if(m > n):
            return self.getKth(b, a, k)
        if not a:
            return b[k-1]
        if k == 1:
            return min(a[0], b[0])
        i = min(k // 2, m)
        j = k - i
        if a[i-1] < b[j-1]:
            return self.getKth(a[i:], b, j)
        elif a[i-1] > b[j-1]:
            return self.getKth(a, b[j:], i)
        else:
            return a[i-1]
