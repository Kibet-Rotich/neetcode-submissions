class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(numbers)):
            if numbers[i] in complements.keys():
                return [complements[numbers[i]]+1,i+1]
            else:
                complements[target-numbers[i]] = i
