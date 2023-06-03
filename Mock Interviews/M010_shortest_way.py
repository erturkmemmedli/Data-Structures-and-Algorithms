# Mock Interview with Bahruz Abil (Microsoft)

Shortest Way to Form String

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        # if set(target) - set(source):
        #     return -1
        
        count = 0
        tarIdx = 0
        
        while tarIdx < len(target):
            
            flag = tarIdx
            
            for srcIdx in range(len(source)):
                
                if target[tarIdx] == source[srcIdx]:
                    
                    tarIdx += 1
                    
                    if tarIdx == len(target):
                        break

                
            if flag == tarIdx:
                return -1
                    
            count += 1
                    
        return count
