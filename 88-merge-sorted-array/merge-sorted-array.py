class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers for nums1, nums2, and the merged array.
        p1 = m - 1  # Pointer for the last actual element in nums1
        p2 = n - 1  # Pointer for the last element in nums2
        p_merged = m + n - 1  # Pointer for the end of nums1 (where we'll place the merged elements)

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merged] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merged] = nums2[p2]
                p2 -= 1
            p_merged -= 1

        # If there are any remaining elements in nums2, copy them over.
        # This happens if nums2 has smaller elements than all elements in nums1.
        while p2 >= 0:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
            p_merged -= 1

        # If there are remaining elements in nums1 (p1 >= 0), they are already in their correct sorted positions.
        # So, no explicit action is needed for them.

