class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i in s:
            dic1[i]+=1
        for j in t:
            dic2[j]+=1
        return dic1==dic2