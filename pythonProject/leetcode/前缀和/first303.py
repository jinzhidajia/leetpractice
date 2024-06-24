class NumArray(object):

    # 前缀和是预处理，所以把处理过程写到 init里面，这样只会初始化一次
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self修饰的字段可在生命周期内保持一致性，可被其他方法所访问
        self.nums = nums
        self.prefix_sum = [0] * (len(nums ) + 1)

        for i in range( len(nums) ):
            self.prefix_sum[i + 1] = nums[i] + self.prefix_sum[i]


    # prefix_sums[i]是0 - (i-1)的前缀和，所以如果要到j就是 prefix_sums[j + 1]，
    # 同理左边要算在里面，而 prefix_sum[i]是指 0 - (i-1)的前缀和
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum[right+1] - self.prefix_sum[left]

# 使用示例
nums = [1, 2, 3, 4, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(1, 3))
print(numArray.sumRange(2, 4))