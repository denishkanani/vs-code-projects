class Solution(object):
    def findMedianSortedArrays(self, nums1 , nums2):
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        
        if n % 2 == 1:
            return nums3[n // 2]
        else:
            return (nums3[n // 2 - 1] + nums3[n // 2]) / 2.0
        
obj = Solution()

nums1 = [1,2]
nums2 = [3,4]

print(obj.findMedianSortedArrays(nums1, nums2))