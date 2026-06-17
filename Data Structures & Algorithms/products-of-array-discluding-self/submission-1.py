class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for n in nums:
            prefix.append(prefix[-1]*n)
        suffix = [1]
        for n in nums[::-1]:
            suffix.append(suffix[-1]*n)
        suffix = suffix[::-1]
        res = []
        for i in range(0, len(prefix)-1):
            res.append(prefix[i]*suffix[i+1])
        return res