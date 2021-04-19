class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        length = len(nums)
        res = 2**100
        result = 0
        for i in range(length-2):
            j = i+1
            k = length-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>target:
                    if nums[i]+nums[j]+nums[k]-target<res:
                        result = nums[i]+nums[j]+nums[k]
                    res = min(nums[i]+nums[j]+nums[k]-target,res)
                    k-=1
                elif nums[i]+nums[j]+nums[k]<target:
                    if target - nums[i] - nums[j] - nums[k]<res:
                        result = nums[i]+nums[j]+nums[k]
                    res = min(target - nums[i] - nums[j] - nums[k],res)
                    j+=1
                else:
                    return target
        return result




sol = Solution()
nums1 = [-1,2,1,-4]
target = 1
print(sol.threeSumClosest(nums1, target))