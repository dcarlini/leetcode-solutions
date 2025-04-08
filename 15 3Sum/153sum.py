class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        # TODO: Write your code here
        nums = sorted(nums)
        # print(nums)

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:  # skip same element to avoid duplicate triplets
                continue
                
            # value = arr[i]
            # target_sum = arr[i] * -1
            # print(i, "target" , -nums[i])

            self.searchPair(nums, -nums[i], i+1, triplets)

        return triplets

    def searchPair(self, nums, target_sum, p1, triplets):
        # p1 = 0
        p2 = len(nums) - 1
        
        while (p1 < p2):

            current_sum = nums[p1] + nums[p2]
            if (current_sum == target_sum):
            
                triplet = [-target_sum, nums[p1], nums[p2]]
                # triplet = sorted(triplet)
                triplets.append(triplet)
                # print(triplet)

            
                p1 += 1
                p2 -= 1
                while p1 < p2 and nums[p1] == nums[p1 - 1]:
                    p1 += 1  # skip same element to avoid duplicate triplets
                while p1 < p2 and nums[p2] == nums[p2 + 1]:
                    p2 -= 1  # skip same element to avoid duplicate triplets
                # break

            elif target_sum > current_sum:
                p1 += 1  # we need a pair with a bigger sum
            else:
                p2 -= 1  # we need a pair with a smaller sum
