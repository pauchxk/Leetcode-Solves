#Given an integer array nums and an integer k, return true if there are two distinct 
#indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

#this works, but the time complexity is O(n^2) and it exceeds the time limit on large inputs
# def contains_duplicate(nums, k):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] == nums[j] and abs(i-j) <= k and i != j:
#                 return True
#     return False


#alternative approach: O(n) time complexity
def contains_duplicate(nums, k):
    d = {}

    for i, n in enumerate(nums):
        if n in d and abs(i - d[n]) <= k:
            return True
        else:
            d[n] = i
        
    return False


#testing
nums = [1,2,3,1,2,3]
k = 2
print(contains_duplicate(nums, k))