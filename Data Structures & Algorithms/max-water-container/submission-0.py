class Solution:
    def maxArea(self, heights: List[int]) -> int:

        areas = []

        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                area = min(heights[i],heights[j])*(j-i)
                areas.append(area)
        
        maximum = float('-inf')
        for num in areas:
            if num>maximum:
                maximum = num

        return maximum        