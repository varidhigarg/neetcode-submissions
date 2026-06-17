from collections import defaultdict
class Solution:
    def getHash(self, s: str) -> str:
        hash_str = [0] * 26
        for x in s:
            hash_str[ord(x) - ord('a')] += 1
        print(hash_str)
        return "#".join(map(lambda x: str(x), hash_str))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        result = []
        for s in strs:
            data[self.getHash(s)].append(s)
        return list(data.values())