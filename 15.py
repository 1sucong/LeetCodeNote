class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        if len(nums)<3:
            return res
        if nums[0]>0:
            return res
        if len(nums)==3 & nums[0]+nums[1]+nums[2]==0:
            res.append([nums[0]+nums[1]+nums[2]])
            return res
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j]+nums[k]+nums[i]<0:
                    j+=1
                elif nums[j]+nums[k]+nums[i]>0:
                    k-=1
        result = []
        for i in res:
            if i not in result:
                result.append(i)
        return result

sol = Solution()
nums1 = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums1))