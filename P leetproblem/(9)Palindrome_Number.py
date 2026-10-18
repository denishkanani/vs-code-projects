class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]
    
obj = Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(0))