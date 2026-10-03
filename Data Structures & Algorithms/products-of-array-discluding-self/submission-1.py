class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        #creating two array as we go from left to right 

        # looking for multiple on the left and the right for any given digit 

        # E.g. if we have A B C D

        # consider left multiples from left to right 

        # so [ 1, A (for left of B ), A * B (for left of C ), .... ]
        # and same from right to left to consider the right multiplier 
        # generate two empty array first
        left_multiples =  [1]*len(nums)
        right_multiples = [1]*len(nums)
        results = [1]*len(nums)
        for i in range (0,len(nums)):

            if i != 0 : 
                left_multiples[i] =  left_multiples[i-1] * nums[i-1]
                

                right_multiples[len(nums)-1-i] = right_multiples[len(nums)-i] * nums[len(nums)-i]
        # combine them
        for j in range(0,len(nums)): 
            results[j] = left_multiples[j] *right_multiples[j]
        return results

        