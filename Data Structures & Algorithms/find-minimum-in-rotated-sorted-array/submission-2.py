class Solution:
    def findMin(self, nums: List[int]) -> int:

        # compare the start and end value
        start = 0 
        end = len(nums)-1 
        repeat = True
        while repeat == True: 
            if nums[start] <= nums[end] : 
                min_val = nums[start]
                repeat = False

            else: 
                mid_position = start + max(1,(end-start)//2)
                if nums[mid_position] <  nums[end]: 
                    end = mid_position 

                else: 
                    start = mid_position

        return min_val

