#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return "".

def longestCommonPrefix(strs):
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

#or#
# def longestCommonPrefix(strs):
#     prefix = strs[0]

#     for i in range(1, len(strs)):
#         if not prefix:
#             return ""
        
#         for j in range(min(len(strs[i]), len(prefix))):
#             if strs[i][j] != prefix[j]:
#                 prefix = prefix[:j]
#                 break
#             else:
#                 prefix = prefix[:len(strs[i])]

#     return prefix

#testing#
strs = ['flower', 'flow', 'flight']
print(longestCommonPrefix(strs))
strs = ['dog', 'racecar', 'car']
print(longestCommonPrefix(strs))
strs = ['ab', 'a']
print(longestCommonPrefix(strs))
