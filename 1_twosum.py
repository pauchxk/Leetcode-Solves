#Given an array of integers nums and an integer target, return indices of the two 
#numbers such that they add up to target. You may assume that each input would 
#have exactly one solution, and you may not use the same element twice#

nums = [2,7,11,15]
target = 9

#idea: index through nums, for each num find the remainder and check if it is in nums. if yes,
#return index of current num and found num. if not, move to next num#

for i, num in enumerate(nums):
    remainder = target - num
    if remainder in nums:
        if nums.index(remainder) != i:
            print(i, nums.index(remainder))