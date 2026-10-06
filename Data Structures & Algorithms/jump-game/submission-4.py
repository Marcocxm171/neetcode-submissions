class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_proximity = 0

        for i in range(len(nums)): 

            if i > max_proximity : 
                return False 

            new_proximity = i + nums[i]

            if new_proximity > max_proximity: 
                max_proximity = new_proximity

        if max_proximity >= len(nums)-1: 
            return True



        