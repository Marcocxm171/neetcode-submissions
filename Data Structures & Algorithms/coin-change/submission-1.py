class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        table = {}
        def solve(amount): 

            if amount < 0:
                return float("inf")

            if amount == 0: 
                return 0 

            elif amount in table: 
                return table[amount]

            else: 
                best = float("inf")
                for coin in coins: 
                    remain = amount - coin
                    answer = solve(remain)                   
                    
                    best = min(best, 1 + answer)
                table[amount] = best 
                return best 
            
        ans = solve(amount)    
        if ans == float("inf"): 
            return -1
        else: 
            return ans

        


        


        