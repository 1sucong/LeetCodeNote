class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        def help(left,right):
            if nums[left]>target:
                return left
            if nums[right]<target:
                return right+1
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                return help(mid+1,right)
            elif nums[mid]>target:
                return help(left,mid)
        s = help(left,right)
        return s
nums = [1,3,5,6]
target = 5
sol = Solution()
print(sol.searchInsert(nums,target))