class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        
        if not s:
            return 0
        
        sign = 1
        i = 0
        num = 0
        
        if s[0] == "-":
            sign = -1
            i = 1
        elif s[0] == "+":
            i = 1
            
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            
        num *= sign
        
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        
        
        return num
    
obj = Solution()
print(obj.myAtoi("42"))
print(obj.myAtoi("-42"))
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("words 987"))
print(obj.myAtoi("9924202324"))