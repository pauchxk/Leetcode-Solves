#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,5,6]
target = 2

if target in nums:
    for i, num in enumerate(nums):
        if num == target:
            print(i)

else:
    nums.append(target)
    nums.sort()
    for i, num in enumerate(nums):
        if num == target:
            print(i)

#alternatively:

for i in range(len(nums)):
    if nums[i] > target or nums[i] == target:
        return i
return len(nums)