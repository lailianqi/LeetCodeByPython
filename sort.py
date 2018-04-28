import heapq


class heap_sort:
    def sort(self, nums):
        m = len(nums)
        for i in range(m//2-1, -1, -1):
            self.adjust_heap(nums, i, m)
        for i in range(m-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.adjust_heap(nums, 0, i)

    def adjust_heap(self, nums, parent, length):
        temp, childpos = nums[parent], 2*parent+1
        while childpos < length:
            rightpos = childpos+1
            if rightpos < length and nums[rightpos] >= nums[childpos]:
                childpos = rightpos
            if nums[childpos] < temp:
                break
            else:
                nums[parent] = nums[childpos]
                parent = childpos
            childpos = 2*parent+1
        nums[parent] = temp


a = [1, 7, 3, 5, 4, 0]
s = heap_sort()
s.sort(a)
print(a)
print("end")
