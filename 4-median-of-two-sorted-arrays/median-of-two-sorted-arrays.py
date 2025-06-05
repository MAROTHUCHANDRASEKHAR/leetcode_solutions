class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lst = []
        l = len(nums1) + len(nums2)
        if l % 2 == 0:
            lst.append(l//2)
            lst.append((l//2)-1)
        else:
            lst.append(l//2)
        
        nums = nums1 + nums2
        nums.sort()
        temp = 0
        if len(lst) != 1:
            for i in lst:
                temp += nums[i]
            return temp / 2
        else:
            return nums[lst[0]]