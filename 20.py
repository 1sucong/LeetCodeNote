class Solution:
    def isValid(self, s: str) -> bool:
        mapdict = {')':'(',']':'[','}':'{'}
        stack = []
        if len(s)%2==1:
            return False
        for i in s:
            if i not in mapdict:
                stack.append(i)
            elif i in mapdict and stack:
                if stack[-1]==mapdict[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return not stack
sol = Solution()
s = "()[]{}"
print(sol.isValid(s))