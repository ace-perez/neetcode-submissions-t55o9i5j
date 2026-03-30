from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_set = defaultdict(int)
        s_set = defaultdict(int)

        for i in s:
            s_set[i] += 1
        
        for i in t:
            t_set[i] += 1

        if s_set == t_set:
            return True

        return False

        