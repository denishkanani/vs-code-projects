class Solution(object):
    def twoSum(self, nums, target):
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] == target:
                    return [a, b]           
obj = Solution()

nums = [1,3,5,7]
target = 8

print(obj.twoSum(nums, target))
