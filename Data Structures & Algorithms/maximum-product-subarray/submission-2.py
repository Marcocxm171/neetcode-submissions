class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        global_min = min(nums)
        global_max = max(nums)

        for i in range(0,len(nums)): 
            
            case = []
            if i == 0 : 
                current_min = nums[i]
                current_max = nums[i]
            
            else: 
                # compute all the possibilites and pick min max 
                case.append(nums[i]*current_min)
                case.append(nums[i]*current_max)
                case.append(nums[i])
                current_max = max(case)
                current_min = min(case)

                if current_max > global_max : 
                    global_max = current_max

        return global_max




            