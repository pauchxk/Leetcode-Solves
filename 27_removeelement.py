#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements 
#may be changed. Then return the number of elements in nums which are not equal to val. Consider the number of elements 
#in nums which are not equal to val be k, to get accepted, you need to do the following things: Change the array nums 
#such that the first k elements of nums contain the elements which are not equal to val. The remaining elements 
#of nums are not important as well as the size of nums. Return k.

def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k


#testing#
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))

nums = [7,25,21,2,20,7,24,9,24,24,6,22,5,1,26,17,18,29,25,9,8,27,6,26,8,5,27,5,0,29,26,29,24,18,23,14,25,17,15,20,11,22,4,17,15,0,26,3,21,21,12,0,10,10,26,19,15,23,16,7,14,12,7,8,0,0,14,26,18,22,8,21,6,12,0,21,4,26,16,26,18,21]
val = 26
print(removeElement(nums, val))