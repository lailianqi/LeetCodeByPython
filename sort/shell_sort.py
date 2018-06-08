class Shell_sort:
    '''
    shell排序
    :type nums: List[int] 要排序的数组
    '''

    def sort(self, nums):
        '''
        :type nums: List[int] 要排序的数组
        '''
        m = len(nums)
        gap = m//2
        while gap > 0:
            for i in range(gap, m):
                j = i
                while j - gap >= 0 and nums[j] < nums[j - gap]:
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]
                    j = j - gap
            gap = gap//2

    def sort_2(self, nums):
        m = len(nums)
        gap = m//2
        while gap > 0:
            for i in range(gap, m):
                j, key = i, nums[i]
                while j - gap >= 0 and key < nums[j - gap]:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = key
            gap //= 2


if __name__ == '__main__':
    print("start")
    a = [1, 7, 3, 5, 4, 0]
    s = Shell_sort()
    s.sort_2(a)
    print(a)
    print("end")
