#given a large integer represented as an integer array digits. increment it by 1 and return the resulting array.
digits = [1,2,3]

last_digit_index = len(digits)-1
last_digit = digits[last_digit_index]

if last_digit == 9:
    if len(digits) == 1:
        digits[last_digit_index] = 1
        digits.append(0)
    else:
        digits[last_digit_index-1] += 1
        digits[last_digit_index] = 0
else:
    digits[last_digit_index] += 1

print(digits)

#^^^ this is inefficient because it is tailored for individual testcases. below is a redesigned algorithm that converts
#the array to an integer in order for the mathematical logic to work properly.

