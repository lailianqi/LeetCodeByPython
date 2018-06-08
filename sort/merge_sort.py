class Merge_sort:
    '''
    归并排序
    '''

    def sort(self, nums):
        '''
        : type nums: List[int] 要排序的数组
        '''
        self.merge_sort(nums, 0, len(nums)-1)

    def merge_sort(self, nums, left, right):
        if left < right:
            mid = (left + right)//2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid+1, right)
            self.merge_arr(nums, left, mid, right)

    def merge_arr(self, nums, left, mid, right):
        m = right - left + 1
        helper_arr = [0]*m
        i, j = left, mid+1
        for k in range(m):
            if self.less(nums, i, j, mid, right):
                helper_arr[k] = nums[i]
                i += 1
            else:
                helper_arr[k] = nums[j]
                j += 1

        for i in range(left, right+1):
            nums[i] = helper_arr[i - left]

    def less(self, nums, i, j, mid, right):
        if j > right or (i <= mid and nums[i] <= nums[j]):
            return True
        return False


if __name__ == '__main__':
    print("start")
    a = [1, 7, 3, 5, 4, 0, 20, 5]
    s = Merge_sort()
    s.sort(a)
    print(a)
    print("end")
