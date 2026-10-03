class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        nums = sorted(set(nums))
        print(nums)

        if len(nums) > 0:
            count = 1 
            max_count = 1 

            for i in range(1,len(nums)): 
                if nums[i] - nums[i-1] == 1 :
                    count += 1
                    if count > max_count: 
                        max_count = count
                else: 
                    count = 1
        else:
            max_count = 0

        return max_count
        