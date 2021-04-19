class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                left = i-1
                for j in range(len(nums)-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        right = j
                        tmp = nums[right]
                        nums[right]=nums[left]
                        nums[left]=tmp
                        numsend = nums[left+1:len(nums)]
                        numsend.sort()
                        return nums[:left+1]+numsend
        return nums.sort()
#从后往前遍历，找到第一对降序，说明后面比前面大，找到左指针，再从后往前遍历第一个比它大的做交换 
sol = Solution()
s = [1,3,2]

print(sol.nextPermutation(s))