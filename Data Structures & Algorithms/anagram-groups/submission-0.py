class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            if key  in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = []
                groups[key].append(strs[i])


        grouped = []
        for key,val in groups.items():
            grouped.append(val)
        return grouped
