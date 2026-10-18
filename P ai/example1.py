class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                x = -(nums[i] + nums[j])

                if x in nums[j + 1:]:
                    res.add((nums[i], nums[j], x))

        return [list(t) for t in res]
    
# Example usage:
solution = Solution()
result = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]