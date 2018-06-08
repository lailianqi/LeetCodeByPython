class Select_sort:
    '''
    选择排序
    '''

    def sort(self, nums):
        '''
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        for i in range(m):
            mid_index = i
            for j in range(i, m):
                if nums[mid_index] > nums[j]:
                    mid_index = j
            nums[i], nums[mid_index] = nums[mid_index], nums[i]


if __name__ == '__main__':
    print("start")
    a = [1, 7, 3, 5, 4, 0]
    s = Select_sort()
    s.sort(a)
    print(a)
    print("end")
