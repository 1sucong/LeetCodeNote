class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []
        
        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return 
            for j in range(i, n):
                if tmp_sum + candidates[j]  > target : break
                if j > i and candidates[j] == candidates[j-1]:continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
        backtrack(0, 0, [])    
        return res

sol = Solution()
candidates = [2,3,4,5,7]
target = 7
print(sol.combinationSum(candidates, target))
