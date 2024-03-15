#Given an integer array nums, return an array answer such that answer[i] is equal 
#to the product of all the elements of nums except nums[i].

nums = [1,2,3,4]

n = len(nums)
left = [1] * n
right = [1] * n

for i in range(1, n):
    left[i] = left[i-1] * nums[i-1]

for i in range(n - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]

result = [left[i] * right[i] for i in range(n)]
print(result)