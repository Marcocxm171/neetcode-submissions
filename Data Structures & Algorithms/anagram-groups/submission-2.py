class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # setup hash map first 

        seen = {}
        max_count = 0 
        max_cat =''

        for i in range(len(strs)): 

            ordered = str(sorted(list(str(strs[i]))))

            if ordered in seen: 
                temp = seen.pop(ordered)
                temp.append(strs[i])
                seen[ordered] = temp
            else: 
                seen[ordered] = [strs[i]]

        
        anagram = []

        for value in seen.values():  
            anagram.append(value)

        return anagram
            

            


        