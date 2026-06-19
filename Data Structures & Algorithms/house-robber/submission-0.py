class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0 , 0]
        for n in nums:
            arr.append(max(arr[-1], arr[-2]+n))
        return arr[-1]
        