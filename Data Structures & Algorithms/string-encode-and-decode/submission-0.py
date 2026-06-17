class Solution:

    def encode(self, strs: List[str]) -> str:
        data = []
        for s in strs:
            data.append(str(len(s)) + '#')
            data.append(s)
        return "".join(data)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j+=1
            count = int(s[i:j])
            result.append(s[j+1:j+1+count])
            i = j+1+count
        return result
