class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        for i in strs:
            str1 += str(len(i))
            str1 += "#"
            str1 += i
        return str1

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        length=""
        while(i<len(s)):
            if(s[i]!="#"):
                length+=s[i]
                i += 1
            else:
                result.append(s[i+1:i+1+int(length)])
                i += 1+int(length)
                length=""
        return result
            
