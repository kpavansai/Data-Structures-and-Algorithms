class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        maxi = 0
        sum = 0
        
        for val in weights:
            sum += val
            maxi = max(maxi, val)
            
        if len(weights) == days:
            return maxi
        
        lo = maxi
        
        hi = sum
        
        ans = 0
        
        while(lo <= hi):
            mid  = (hi + lo)//2
            
            if self.possible(weights, mid, days) == True:
                
                ans = mid
                
                hi = mid - 1
                
            else:
                
                lo = mid + 1
                
        return ans
    
    
    def possible(self, wt, mid, days):
        
        d = 1
        sumNew = 0
        
        for i in range(0, len(wt)):
            
            sumNew += wt[i]
            
            if sumNew > mid:
                d += 1
                sumNew = wt[i]
                
        return d <= days