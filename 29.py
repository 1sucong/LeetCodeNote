class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absend = abs(dividend)
        absor = abs(divisor)
        res = 0
        while absend>absor:
            absend -= absor    
            res+=1

        strdividend = str(dividend)
        strdivisor = str(divisor)
        if strdividend[0]=='-' and strdivisor[0]=='-':
            return res
        if strdividend[0]=='-' or strdividsor[0]=='-':
            return res*(-1)
        return res

sol = Solution()
print(sol.divide(7,-3))