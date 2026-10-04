class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count them up first
        nums = sorted(nums)
        unique = sorted(list(set(nums)))
        table = [[] for i in range(len(nums)+1)]
        top_k = []
        running_count = 1
        unique_idx = 0 

        if len(nums) == 1: 
            table[1].append(nums[0])
        else: 
            for i in range(1,len(nums)):
                if nums[i] == nums[i-1] and i == len(nums)-1 :
                    running_count += 1
                    table[running_count].append(unique[unique_idx])         
                elif nums[i] == nums[i-1]: 
                    running_count += 1
                elif nums[i] != nums[i-1] and i != len(nums)-1 :
                    table[running_count].append(unique[unique_idx])
                    running_count = 1
                    unique_idx += 1
                elif nums[i] != nums[i-1] and i == len(nums)-1 :
                    table[running_count].append(unique[unique_idx])
                    running_count = 1
                    unique_idx += 1
                    table[running_count].append(unique[unique_idx])

            
             

        # bucket sort- extract top k
        count = 0 
        for i in range(len(nums)+1):
            if table[len(nums)-i] != [] and count < k: 
                for j in range(len(table[len(nums)-i])):
                    top_k.append(table[len(nums)-i][j])
                count += len(table[len(nums)-i])

        return top_k   