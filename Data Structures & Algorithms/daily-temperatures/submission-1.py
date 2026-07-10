class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result=[]
        for i in range(len(temperatures)):
            found = False
            j=i+1
            while(j<len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    found=True
                    break
                else:
                    j+=1
            if not found:
                result.append(0)
        return result
                

        