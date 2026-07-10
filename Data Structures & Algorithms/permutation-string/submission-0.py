class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        list1 = list(s1)
        set1 = set(list1)

        for i in range(len(s2)):
            if s2[i] in set1:
                if sorted(s2[i:i+len(s1)]) ==  sorted(s1):
                    return True
                
        return False

        