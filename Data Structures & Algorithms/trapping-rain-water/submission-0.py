class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max =[float('-inf')]*len(height),[float('-inf')]*len(height)
        maxval = float('-inf')
        for i,left in enumerate(height):
            left_max[i] = maxval
            maxval = max(left,maxval)
            
        maxval = float('-inf')
        for right in range(len(height)-1,-1,-1):
            right_max[right] = maxval
            maxval = max(height[right],maxval)
        volume = 0
        for i,val in enumerate(height):
            vol_i = max(0,min(left_max[i],right_max[i])-val)
            volume +=vol_i
        
        return volume

            
        

        
