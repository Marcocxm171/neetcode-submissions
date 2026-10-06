class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        s = list(s)
        start = 0 
        end = 1
        seen = {}
        seen[s[0]] = 1
        majority_count = 1 
        majority = s[0]
        max_length = 1

        while end < len(s) and start < end:

            # append the hashmap  
            if s[end] in seen: 
                seen[s[end]] += 1

            else: 
                seen[s[end]] = 1 

            # decide who is the majority now 
            majority_count = max(seen.values())

            #tighten window until we want to try next
            # check how many replacement we need: 
            length = end-start + 1
            r_needed = length - majority_count 

            if r_needed <= k : 
                
                if max_length < length: 
                    max_length = length
                end += 1 
            
            elif r_needed > k :

                # need to remove starting value we are dropping
                while r_needed > k and start < end: 
                    seen[s[start]] -= 1
                    start += 1
                    if majority == s[start]: 
                        majority_count -= 1

                    # decide who is the majority now 
                    majority_count = max(seen.values())
                    
                    length = end-start + 1
                    r_needed = length - majority_count 

                end += 1
                    

                # check whether we can stabilise the start again 
        
        return max_length  


            



        