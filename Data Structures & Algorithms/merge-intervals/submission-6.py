class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        # first sort the intervals

        intervals.sort()
        anchor = 0 
        tracer = 1
        new_interval = []

        while anchor < len(intervals): 

            current_start = intervals[anchor][0]
            current_end = intervals[anchor][1]

            no_overlap = True
            while no_overlap == True and tracer < len(intervals):  
                #check whether it is overlapped
                if current_start <= intervals[tracer][0] <= current_end :
                    current_end = max(current_end,intervals[tracer][1])
                    tracer += 1
                else: 
                    no_overlap = False

            new_interval.append([current_start,current_end])
            anchor = tracer 

        return new_interval 
        