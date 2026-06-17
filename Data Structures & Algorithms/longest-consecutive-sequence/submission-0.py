class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        seq_starts = []
        for n in nums:
            if n-1 not in data:
                seq_starts.append(n)
        result = 0
        for x in seq_starts:
            local_res = 0
            while x in data:
                x+=1
                local_res+=1
            result = max(result, local_res)
        return result
        