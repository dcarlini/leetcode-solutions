class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nextPos = len(nums1) - 1
        p1 = m - 1
        p2 = n - 1

        
        while (p1 >= 0 or p2 >= 0):

            if p2 < 0:
                break

            if (p1 >= 0 and nums1[p1] > nums2[p2]):
                nums1[nextPos] = nums1[p1]
                nextPos -= 1
                p1 -= 1
            else: # nums1[p1] < nums2[p2]:
                nums1[nextPos] = nums2[p2]
                nextPos -= 1
                p2 -= 1
            
            
         



            




      

    

        
        