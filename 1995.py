class Solution:
    def permutation(self, S: str):
        length = len(S)
        res = []
        used = [False]*length
        def back(used,tmp):
            if len(tmp)==length:
                res.append(''.join(tmp))
                return
            for i in range(length):
                if used[i]:
                    continue
                used[i]=True
                tmp.append[S[i]]
                back(used,tmp)
                used[i]=False
                tmp.pop()
        back(used,[])
        return res

sol = Solution()
S = "qwe"
sol.permutation(S)