from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        freq_sorted = sorted(count.values(), reverse = True)

        res = 0
        multiplier = 1
        for i in range(len(freq_sorted)):
            res += freq_sorted[i] * multiplier
            if (i + 1) % 8 == 0:
                multiplier += 1
        
        return res