class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums:
                current = num
                streak = 1
                while current+1 in nums:
                    current+=1
                    streak+=1
                longest = max(longest,streak)
        
        return longest


        