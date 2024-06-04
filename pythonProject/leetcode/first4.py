
# 双指针？滑动窗口？
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        left = 0
        ans = ''
        for right in range(len(s)):
