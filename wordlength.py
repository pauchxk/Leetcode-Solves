#given a string 's' consisting of words and spaces, return the length of the last word in the string.
s = 'Hello World'

splits = s.split()

wrd_loc = int(len(splits) - 1)

print(len(splits[wrd_loc]))