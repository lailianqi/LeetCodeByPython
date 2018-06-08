class Insert_sort:
    '''
    插入排序
    :type nums: List[int] 要排序的数组
    '''

    def sort(self, nums):
        '''
        用swap的插入排序
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        for i in range(m):
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1


    def sort_2(self, nums):
        '''
        标准插入排序
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        for i in range(m):
            key = nums[i]
            j = i-1
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key


if __name__ == '__main__':
    print("start")
    a = [1, 7, 3, 5, 4, 0]
    s = Insert_sort()
    s.sort_2(a)
    print(a)
    print("end")
