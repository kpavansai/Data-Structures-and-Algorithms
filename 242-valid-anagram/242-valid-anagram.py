class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        
        for words in s:
            if words not in mapS:
                mapS[words] = 1
            else:
                mapS[words] += 1
                
        mapT = {}
        for wordsT in t:
            if wordsT not in mapT:
                mapT[wordsT] = 1
            else:
                mapT[wordsT] += 1
        
        if mapS == mapT:
            return True
        else:
            return False
        
        
        
#         map_s = {}
#         for items in s:
#             if items not in map_s:
#                 map_s[items] = 1
#             else:
#                 map_s[items] += 1
#         map_t = {}
#         for itemt in t:
#             if itemt not in map_t:
#                 map_t[itemt] = 1
#             else:
#                 map_t[itemt] += 1
                
#         if map_s == map_t:
#             return True
#         else: return False
        
                