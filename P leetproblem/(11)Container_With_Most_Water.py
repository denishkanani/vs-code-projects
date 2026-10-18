class Solution(object):
    def maxArea(self, height):
        ans = 0
        
        for a in range(len(height)):
            for b in range(a + 1, len(height)):
                area = min(height[a], height[b]) * (b - a)
                if area > ans:
                    ans = area
                    
        return ans
    
    
obj = Solution()                
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))