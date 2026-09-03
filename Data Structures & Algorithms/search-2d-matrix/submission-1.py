class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix),len(matrix[0])
        low,high = 0, m*n -1
        
        while low<=high:
            mid = low+(high-low)//2
            targetrow = mid//n
            targetcol = mid%n
            if matrix[targetrow][targetcol] == target:
                return True
            elif  matrix[targetrow][targetcol] < target:
                low = mid +1
            else:
                high = mid-1
        
        return False

        