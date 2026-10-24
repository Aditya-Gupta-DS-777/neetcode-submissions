class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rr = defaultdict(list)
        for s in strs:
            sr = ''.join(sorted(s))
            rr[sr].append(s)
        return list(rr.values())