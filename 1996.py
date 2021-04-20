class Solution:
    def permutation(self, S: str):
        if not S or len(S) <= 1: return []

        res, S, length = [], sorted(S), len(S)  # 排下序，使重复的都在一起

        def backtrack(used, paths):
            if length == len(paths):
                res.append(''.join(paths))
                return

            for i in range(length):
                if used[i]:
                    continue  # 已经选择过的不需要再放进去了
                if i > 0 and S[i] == S[i - 1] and not used[i - 1]:
                    continue  # 如果当前节点与他的前一个节点一样，并其他的前一个节点已经被遍历过了，那我们也就不需要了。

                used[i] = True
                paths.append(S[i])
                backtrack(used, paths)
                used[i] = False
                paths.pop()

        backtrack([False] * length, [])
        return res

sol = Solution()
S = "qqe"
sol.permutation(S)