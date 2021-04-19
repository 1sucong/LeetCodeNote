class Solution:
    def searchRange(self, nums, target: int):
        left = 0
        right = len(nums)-1
        res = []
        while left<right:
            mid = (left+right)//2
            if nums[mid]==target:
                resleft = mid
                resright = mid
                while resleft>0:
                    resleft-=1
                    if nums[resleft]!=target:
                        break
                while resright<len(nums)-1:
                    resright+=1
                    if nums[resright]!=target:
                        break
                
                
                res.append(resleft)
                res.append(resright)
                return res
            elif nums[mid]>target:
                right = mid
            else:
                left = mid+1
        return [-1,-1]
nums = [2,2]
target = 2
sol = Solution()
print(sol.searchRange(nums,target))