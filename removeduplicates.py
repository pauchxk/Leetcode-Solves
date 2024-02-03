#given a sorted integer array nums, remove the duplicates in place. relative order should be
#kept the same. then return the number of unique elements in nums.

nums = [0,0,1,1,1,2,2,3,3,4]

checknums = []

for num in nums:

    if num not in checknums:
        checknums.append(num)

    elif num in checknums:
        nums.remove(num)
        num -= 1
    
print('checknums',checknums)

print(str(len(nums))+',','nums =',nums)

#^^^ this doesn't work. a more elegant solution by Alvie in the uni discord:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0
        prev_num = "X"

        for i in range(len(nums)):
            if nums[i] != prev_num:
                nums[unique_count] = nums[i]
                unique_count += 1
                prev_num = nums[i]

        # Stupid part because leetcode is not returning correctly
        return unique_count
        # return nums_to_return

