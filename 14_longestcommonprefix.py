#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return "".

strs = ["flower", "flow", "flight"]

prefix = strs[0]
for string in strs[1:]:
    while string.find(prefix) != 0:
        prefix = prefix[:-1]
        if not prefix:
            print("")
print(prefix)