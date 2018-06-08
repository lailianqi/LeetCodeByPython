import heapq
from Bubble_sort import Bubble_sort


class Heap_sort:
    '''
    堆排序
    '''

    def sort(self, nums):
        '''
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        for i in range(m//2-1, -1, -1):
            self.adjust_heap(nums, i, m)
        for i in range(m-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.adjust_heap(nums, 0, i)

    def adjust_heap(self, nums, parent, length):
        '''
        堆调整算法
        :type nums: List[int] 要排序的数组
        :type parent: int 要调整的父节点
        :type length: int 要调整的数组长度
        '''
        orgin_parent_value, childpos = nums[parent], 2*parent+1
        while childpos < length:
            rightpos = childpos+1
            if rightpos < length and nums[rightpos] >= nums[childpos]:
                childpos = rightpos
            if nums[childpos] < orgin_parent_value:
                break
            else:
                nums[parent] = nums[childpos]
                parent = childpos
            childpos = 2*parent+1
        nums[parent] = orgin_parent_value


if __name__ == '__main__':
    a = [1, 7, 3, 5, 4, 0]
    s = Bubble_sort()
    s.sort_optimize(a)
    print(a)
    print("end")
