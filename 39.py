class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []

        def helper(candidates, target, temp_list):
            
            if target == 0:
                res.append(temp_list)
                return
            if target < 0:
                return
            for i in candidates:
                if i > target:
                    break
                helper(candidates, target-i, temp_list+[i])

        helper(candidates, target, [])       
        return res


sol = Solution()
candidates = [2,3,4,5,7]
target = 7
print(sol.combinationSum(candidates, target))
