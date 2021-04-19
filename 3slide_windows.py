class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

# 滑动窗口，定义左游标（用于删除字典里面对应的数），字典，最大长度，当前长度
# 循环所有元素，一直添加到lookup，并且更新当前长度，大于最大长度时做更换
# while遇到在字典里，则从字典里删去左右标对应元素，并更新左游标，当前长度

s = 'abcabc'
        
