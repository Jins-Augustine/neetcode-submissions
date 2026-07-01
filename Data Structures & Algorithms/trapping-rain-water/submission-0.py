class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        leftmax = [0]*h
        rightmax = [0]*h

        leftmax[0] = height[0]
        rightmax[h-1] = height[h-1]

        for i in range(1,h):
            leftmax[i] = max(leftmax[i-1],height[i])
        
        for i in range(h-2,-1,-1):
            rightmax[i] = max(rightmax[i+1],height[i])
        
        water=0
        for i in range(h):
            water += min(leftmax[i],rightmax[i]) - height[i]
        
        return water

        