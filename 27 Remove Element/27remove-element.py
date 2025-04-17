class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1

        if len(nums) == 1:
            return nums[0] != val

        while p1 <= p2:
            i = nums[p1]

            if i == val:
                temp = nums[p2]
                nums[p2] = i
                nums[p1] = temp
                p2 -= 1
            else :        
                p1 += 1
        
        if p2 >= 0:
            p2 += 1
        else:
            p2 = 0
        
        return p2
        
            
            
                
        