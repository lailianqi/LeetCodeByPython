class Bubble_sort:
    '''
    冒泡排序
    '''

    def sort(self, nums):
        '''
        标准版冒泡排序
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        for i in range(m-1, -1, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    def sort_optimize(self, nums):
        '''
        优化版冒泡排序
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        for i in range(m-1, -1, -1):
            is_sorted = True
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_sorted = False
            if is_sorted:
                break