class Solution(object):
    def longestPallindrome(self, s):
        ans = ""
        
        for a in range(len(s)):
            for b in range(a, len(s)):
                temp = s[a:b+1]
                
                if temp == temp[::-1] and len(temp) > len(ans):
                    ans = temp
                    
        return ans
    
obj = Solution()
print(obj.longestPallindrome("racecar"))
print(obj.longestPallindrome("abchedaba"))
print(obj.longestPallindrome("a"))