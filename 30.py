from collections import Counter

class Solution:
    def findSubstring(self, s: str, words):
        cnt = Counter()
        res = []
        for i in words:
            cnt[i]=cnt[i]+1
        lenword = len(words[0])
        lenwords = lenword*len(words)
        for i in range(len(s)-lenwords+1):
            tempres = s[i:i+lenwords]
            tempcnt  = Counter()
            for j in range(0,len(tempres)-lenword+1,lenword):
                tempcnt[tempres[j:j+lenword]] +=1
            if tempcnt == cnt:
                res.append(i)
        return res

            

sol = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(sol.findSubstring(s,words))