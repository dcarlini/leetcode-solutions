class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)

        upper_pairs = self.countPairsWithSumLessThan(nums, upper + 1)
        lower_pairs = self.countPairsWithSumLessThan(nums, lower)

        return upper_pairs - lower_pairs

    def countPairsWithSumLessThan(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count
        