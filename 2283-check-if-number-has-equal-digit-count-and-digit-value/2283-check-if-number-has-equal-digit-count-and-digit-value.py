class Solution:
    def digitCount(self, num: str) -> bool:
        
        map1 = {}
        
        map2 = {}
        
        for i in range(len(num)):
            
            map1[i] = num[i]
            
            map2[i] = str(num.count(str(i)))
            
        return map1 == map2