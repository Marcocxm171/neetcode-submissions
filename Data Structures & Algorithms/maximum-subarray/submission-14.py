class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initially start = 0 
        start = 0 
        max_count = max(nums)
        end = 1
        running_sum = nums[start]
        while start < len(nums)-2 and end < len(nums):

            running_sum += nums[end]

            if running_sum <= 0: 
                start +=  1
                end = start + 1
                running_sum = nums[start]

            else: 
                end += 1                
            
            if running_sum > max_count: 
                    max_count = running_sum

        return max_count



           

                
                
                
        