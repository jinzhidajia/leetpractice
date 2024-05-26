class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [ i , hashtable[target - nums[i]] ]
            hashtable[nums[i]] = i
        return []

def main():
    nums = [2, 7, 11, 15]
    target = 2
    solution = Solution()
    print(solution.twoSum(nums,target))

if __name__ == '__main__':
    main()