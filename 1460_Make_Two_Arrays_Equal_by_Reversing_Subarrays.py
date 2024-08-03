from collections import Counter

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        count_arr = Counter(arr)
        count_target = Counter(target)

        if count_arr != count_target:
            return False
        
        return True
        