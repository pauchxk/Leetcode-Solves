#given a roman numeral, convert it to an integer.
#time complexity: O(n) n = length of s
#space complexity: O(n) n = length of s

def romanToInt(s):

    numeral_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    exceptions_dict = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    output = 0
    for i in range(len(s)):

        try:
            combo = s[i] + s[i+1]
        except:
            combo = 0

        if i > 0:
            prev_combo = s[i-1] + s[i]
        else:
            prev_combo = 0

        if prev_combo in exceptions_dict:
            continue
        
        elif combo in exceptions_dict:
            output += exceptions_dict[combo]

        else:
            output += numeral_dict[s[i]]

    return output

#infinitely better solution#
def romanToIntBetter(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number


#testing#
s = "III"
print(romanToInt(s))
s = "LVIII"
print(romanToInt(s))
s = "MCMXCIV"
print(romanToInt(s))
s = "MMMCDXC"
print(romanToInt(s))
s = "D"
print(romanToInt(s))