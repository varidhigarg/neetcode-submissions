class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x, y, z = 0, 0, len(nums) - 1
        
        while y <= z:
            if nums[y] == 0:
                nums[y], nums[x] = nums[x], nums[y]
                x+=1
                y+=1
            elif nums[y] == 2:
                nums[y], nums[z] = nums[z], nums[y]
                z-=1
            else:
                y+=1
