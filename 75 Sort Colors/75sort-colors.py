class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        p2 = len(nums) - 1

        i = 0
        while i <= p2:
            if nums[i] == 0:
                tmp = nums[p1]
                nums[p1] = nums[i]
                nums[i] = tmp
                i += 1
                p1 += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                tmp = nums[p2]
                nums[p2] = nums[i]
                nums[i] = tmp
                p2 -= 1

            print (nums, i, p1, p2)
            


        