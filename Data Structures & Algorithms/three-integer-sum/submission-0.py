class Solution:
    def twoSum(self, nums, target):
        data = set()
        res = []
        for i, n in enumerate(nums):
            if target - n in data:
                res.append([n, target-n])
            data.add(n)
        return res
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i, x in enumerate(nums):
            res = self.twoSum(nums[:i] + nums[i+1:], -x)
            for a, b in res:
                result.add(tuple(sorted([a,b,x])))
        return list(result)
