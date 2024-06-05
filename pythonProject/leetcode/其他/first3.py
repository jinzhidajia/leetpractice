## 找子串可以用到滑动窗口
# right从头开始向右边扩张，条件不满足时left收缩
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        # 用来存储子串
        char_set = set()
        left = 0

        # right在向右扩张
        for right in range(len(s)):
            # 检查到不符合条件的左边收缩
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            #不然的话就把right加进结果字典里
            char_set.add(s[right])
            # 比较当前滑动窗口大小和结果
            max_length = max(right - left + 1 ,max_length)

        return max_length


solution = Solution()
ans = solution.lengthOfLongestSubstring("dvdf")
print(ans)
