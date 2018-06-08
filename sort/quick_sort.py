import random


class Quick_sort:

    def sort(self, nums):
        '''
        快速排序
        :type nums: List[int] 要排序的数组
        '''
        self.quick_sort(nums, 0, len(nums)-1)
        # print(sorted(nums))

    def quick_sort(self, nums, left, right):
        '''
        :type nums: List[int] 要排序的数组
        '''
        if left < right:
            index = self.partition(nums, left, right)
            self.quick_sort(nums, left, index-1)
            self.quick_sort(nums, index+1, right)

    def partition(self, nums, left, right):
        # i, j, pivot = left, right+1, nums[left]
        # while i < j:
        #     while nums[i += 1] < pivot and i < right:
        #         pass
        #     while nums[j -= 1] > pivot:
        #         pass
        #     if i >= j:
        #         break
        #     nums[i], nums[j] = nums[j], nums[i]
        # nums[j], pivot = pivot, nums[j]
        # return j
        pivot, i, j = nums[left], left, right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i


if __name__ == '__main__':
    print("start")
    a = [1, 7, 3, 5, 4, 0]
    s = Quick_sort()
    s.sort(a)
    print(a)
    print("end")
