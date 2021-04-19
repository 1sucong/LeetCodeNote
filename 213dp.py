class Solution:
    def rob(self, nums) -> int:
        init_len = len(nums)
        def robhelp(nums):
            lenth = len(nums)
            if lenth==1:
                return nums[-1]
            if lenth==2:
                return max(nums[-1],nums[-2])
            dp = [0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,lenth):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[lenth-1]
        a = robhelp(nums[:init_len-1])
        b = robhelp(nums[1:init_len])
        return max(a,b)

sol = Solution()
nums1 = [2,1,1,2]
print(sol.rob(nums1))