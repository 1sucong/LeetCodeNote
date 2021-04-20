class Solution:
    def firstMissingPositive(self, nums) -> int:
        
        reshash = dict((k,1) for k in nums)
        for i in range(1,len(nums)+1):
            if i not in reshash:
                return i
        
        return max(reshash.keys())+1




sol = Solution()
nums = [2]
print(sol.firstMissingPositive(nums))