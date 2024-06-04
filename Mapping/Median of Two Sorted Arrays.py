# -*- coding = utf-8 -*-
# @Time : 5/2/2023 3:29 PM
# @Author : Lauren
# @File : Median of Two Sorted Arrays.py
# @Software : PyCharm
# binary search

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        list_combined = nums1 + nums2
        list_sorted = sorted(list_combined)
        length = len(list_sorted)
        if length % 2 == 0:
            return (list_sorted[length // 2 - 1] + list_sorted[length //
                                                               2]) / 2
        else:
            return list_sorted[length // 2]

def main():
    my_solution = Solution()
    nums1 = [1, 2, 5]
    nums2 = [3, 9]
    print(my_solution.findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    main()
