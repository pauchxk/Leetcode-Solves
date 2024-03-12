#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

nums1 = [1,3,4]
nums2 = [2]

merged_nums = nums1 + nums2
merged_nums.sort()

half = len(merged_nums) // 2

if len(merged_nums) % 2 != 0:
    print(float(merged_nums[half]))

else:
    median = (merged_nums[half] + merged_nums[half-1]) / 2
    print(median)