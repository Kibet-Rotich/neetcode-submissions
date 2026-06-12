class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myarr = []
        for i in range(len(nums)):
            if nums[i] in myarr:
                return True
            else:
                myarr.append(nums[i])
        return False
        