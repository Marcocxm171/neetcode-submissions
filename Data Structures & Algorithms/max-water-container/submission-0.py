class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start = 0 
        end = len(heights) - 1 
        max_vol = 0 

        while start < end: 

            # calculate the volume and check whether it is new max 

            vol = min(heights[start],heights[end]) *(end-start)

            if max_vol < vol: 
                max_vol = vol

            # check which is shorter

            if heights[start] < heights[end]:
                # we move start
                start += 1 

            else: 
                end -=1 

        return max_vol

