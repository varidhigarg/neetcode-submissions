class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0, 1, 2]
        for x in range(2, n):
            arr.append(arr[-2] + arr[-1])
        return arr[-1] if n >= 2 else arr[n]