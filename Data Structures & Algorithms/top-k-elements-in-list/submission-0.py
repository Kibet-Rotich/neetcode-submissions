class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 0
        
        keys = []
        
        
        

        for i in range(k):
            max = float("-inf")
            
            for key,val in count.items():
                if val> max:
                    max = val
                    topkey = key
            keys.append(topkey)
            del count[topkey]
        return keys
            
            
