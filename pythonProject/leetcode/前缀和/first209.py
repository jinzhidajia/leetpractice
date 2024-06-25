import bisect

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = nums[i] + prefix_sum[i]

        # 按要求 prefix_sum[i]-prefix_sum[j] >= target
        # 所以用二分找第一个满足条件的：required = prefix_sum[i] - target

        min_length = n + 1
        # 遍历前缀和数组
        for i in range(1 , n + 1):
            required_sum = prefix_sum[i] - target
            # 使用二分查找找第一个满足 prefix_sums[j] >= required_sum 的索引j
            # 返回第一个大于taget值
            j = bisect.bisect_left(prefix_sum, required_sum, 0, i)
            if j < i:
                min_length = min(min_length,i-j)

        return min_length

nums = [2, 3, 1, 2, 4, 3]
target = 7
solution = Solution()
print(solution.minSubArrayLen(target,nums))