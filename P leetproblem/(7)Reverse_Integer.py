class Solution(object):
    def reverse(self, x):
        rev = 0
        sign = 1
        
        if x < 0:
            sign = -1
            x = -x
            
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10    
            
        rev = rev * sign
            
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0
    
obj = Solution()
print(obj.reverse(115))
print(obj.reverse(-524))
print(obj.reverse(4500))
print(obj.reverse(1534236469))