from collections import defaultdict
class Solution:
    def getHash(self, s: str) -> str:
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for s in strs:
            data[self.getHash(s)].append(s)
        return list(data.values())