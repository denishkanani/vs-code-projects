class Solution(object):
    def convert(self, s ,numRows):
        if numRows == 1:
            return s
        
        rows = [""] * numRows
        i = 0
        
        while i < len(s):
            for r in range(numRows):
                if i >= len(s):
                    break
                rows[r] += s[i]
                i += 1
                
            for  r in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break
                rows[r] += s[i]
                i += 1
        return "".join(rows)
    
obj = Solution()
print(obj.convert("PAYPALISHIRING", 3))
print(obj.convert("PAYPALISHIRING", 4))
print(obj.convert("A", 1))