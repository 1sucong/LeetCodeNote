class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        lenth = len(s)
        res = 0
        if s[0]=='-':
            for i in range(lenth-1,0,-1):
                res += int(s[i])*pow(10,i-2)
            return res
        for i in range(lenth-1,-1,-1):
            
            res += int(s[i])*pow(10,i)
        return res

sol = Solution()
nums1 = 123
print(sol.reverse(nums1))