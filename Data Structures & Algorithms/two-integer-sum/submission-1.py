class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combo = []
        # implement the two point search method:
        for i in range (len(nums)): 
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target: 
                    combo.append(i)
                    combo.append(j) 

        return combo