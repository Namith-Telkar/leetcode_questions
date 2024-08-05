from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = Counter(arr)
        distinct_strings = []
        
        for s in arr:
            if count[s] == 1:
                distinct_strings.append(s)

        if len(distinct_strings) < k:
            return ""
        else:
            return distinct_strings[k - 1]