class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}
        res = []
        s_len = len(s)

        for i in range(s_len):
            last_index[s[i]] = i

        
        curLen = 0
        goal = 0
        j = 0

        while j < s_len:
            goal = max(goal, last_index[s[j]])
            curLen += 1

            if goal == j:
                res.append(curLen)
                curLen = 0
            
            j += 1
        
        return res
