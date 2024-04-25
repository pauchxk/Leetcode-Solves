#You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following 
#conditions are satisfied: t is a subsequence of the string s. The absolute difference in the alphabet order of every 
#two adjacent letters in t is less than or equal to k. Return the length of the longest ideal string. A subsequence 
#is a string that can be derived from another string by deleting some or no characters without changing the order of 
#the remaining characters. Note that the alphabet order is not cyclic. For example, the absolute 
# difference in the alphabet order of 'a' and 'z' is 25, not 1.

#method#
#1. split s into list of individual chars.
#2. iterate through list and retrieve ASCII value -? to get 1-26.
#3. iterate through list again and check difference between each adjacent value.
#4. if difference is too large, mark index as breakpoint and continue?

def longestIdealString(s, k):
    pass


#testing#
s = "acfgbd"
k = 2
print(longestIdealString(s, k))

s = "abcd"
k = 3
print(longestIdealString(s, k))
