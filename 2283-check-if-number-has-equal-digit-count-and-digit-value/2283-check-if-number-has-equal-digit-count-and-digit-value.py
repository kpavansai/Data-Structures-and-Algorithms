class Solution:
    def digitCount(self, num: str) -> bool:
        result = [0] * 10
        
        for i in num:
            result[int(i)] += 1
            
        for i in range(len(num)):
            if int(num[i]) != result[i]:
                return False
        return True
        