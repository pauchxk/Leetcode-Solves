#given two strings needle and haystack, return the index of the first occurrence of needle
#in haystack, or -1 if needle is not part of haystack.
haystack = 'sadbutsad'
needle = 'sad'

needle_index = haystack.find(needle) #.find returns index of substring within specified string
print(needle_index) #if not found, returns -1. pretty much built to solve this problem. 