#given a string s, find the first non-repeating character in it and return its index. if it does#
#exist, return -1                                                                               #
s = "leetcode"

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for i, char in enumerate(s):
    if freq[char] == 1:
        print(i, char)
        break