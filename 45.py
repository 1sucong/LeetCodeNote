class Solution:
    def jump(self, nums) -> int:
        farthest = 0
        end = 0         # 记录每一步跳跃可以到的区间的最后一个元素，用于记录何时jumps+=1
        jumps = 0       # 记录跳跃次数
        for i in range(len(nums)-1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                jumps += 1
                end = farthest
        return jumps


nums = [2,3,1,1,4]
sol = Solution()
sol.jump(nums)