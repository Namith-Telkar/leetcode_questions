class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        nums = nums + nums
        res = count = total - sum(nums[0:total])
        l, r = 0, total
        while r < len(nums):
            if not nums[r]:
                count += 1
            if not nums[l]:
                count -= 1
            l += 1
            r += 1
            res = min(res, count)
        return res