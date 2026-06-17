class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        data = list(filter(lambda x: x.isalnum(), s))
        return data == data[::-1]