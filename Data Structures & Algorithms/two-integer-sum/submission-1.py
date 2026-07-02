class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complements = {}

        for i in range(len(nums)):
            key = nums[i]
            if key in complements.keys():
                return [complements[key],i]
            else:
                complements[target-key]= i
        
        return []

        