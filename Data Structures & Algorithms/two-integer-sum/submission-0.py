class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()
        for i, val in enumerate(nums):
            if target - val not in data:
                data[val] = i
            else:
                return [data[target - val], i]