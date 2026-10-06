class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s = list(s)
        start = 0 
        end = 1 
        #create a hash map 
        seen = {}
        count = 1
        if len(s) == 0: 
            max_count = 0
        else: 
            max_count = 1
        
            seen[s[start]] = 0

        while end < len(s): 
            
            # check whether is in hashmap
            if s[end] in seen: 
                new_start = max(seen.pop(s[end])+1,start)     
                start = new_start 
                seen[s[end]] = end 
                end += 1
                count = end - start 

            else: 
                seen[s[end]] = end
                count +=  1 
                end += 1

            if count > max_count : 
                max_count = count

        return max_count
            
