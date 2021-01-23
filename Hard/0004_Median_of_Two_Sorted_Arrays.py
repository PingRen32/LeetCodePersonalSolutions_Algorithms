# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m

        if m == 0:
            return median(nums2)
        elif n == 0:
            return median(nums1)
        elif n <= 4:
            return median(nums1 + nums2)
        else:
            size = n // 4
            if nums1[size] < nums2[size]:
                if nums1[-size] > nums2[-size]:
                    return self.findMedianSortedArrays(nums1[size:-size], nums2)
                else:
                    return self.findMedianSortedArrays(nums1[size:], nums2[0:-size])
            else:
                if nums1[-n // 4] > nums2[-n // 4]:
                    return self.findMedianSortedArrays(nums1[0:-size], nums2[size:])
                else:
                    return self.findMedianSortedArrays(nums1, nums2[size:-size])