class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)-1
        mid = len(nums)//2
        found = False

        while start <= end: 

            if nums[mid] == target:
                return mid
                break 

            #check which side is sorted first
            if nums[mid] >= nums[start]:
                # this left is sorted

                if nums[start] <= target < nums[mid]: 
                    # we know that the target is on the sorted side - lock into the left side
                    end = mid - 1

                else: 
                    #we know the target is in the non sorted side
                    start = mid +1

            elif nums[mid] <= nums[end]: 
                # the right side is sorted

                if nums[mid] < target <= nums[end]: 
                    start = mid +1

                else: 
                    end = mid - 1

            

            mid = start + (end - start)//2
        return -1