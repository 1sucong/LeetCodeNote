class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        lenth = len(height)
        i = 0
        j = lenth-1
        while i<j:
            if height[i]>height[j]:
                max_area = max(max_area,(j-i)*height[j])
                j-=1
            else:
                max_area = max(max_area,(j-i)*height[i])
                i+=1
        return max_area

sol = Solution()
nums1 = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(nums1))