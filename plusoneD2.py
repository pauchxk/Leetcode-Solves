#given a large integer represented as an integer array digits. increment it by 1 and return the resulting array.
digits = [1,2,3]

digit_string = ''
new_digits = []

for i in digits:
    digit_string += str(i)

digit_string = int(digit_string)
digit_string += 1
digit_string = str(digit_string)

for i in digit_string:
    new_digits.append(i) #need to find a way to append individual characters of an integer to a list without converting it
                         #to a string as that adds apostrophes. 

print('[' + ', '.join(new_digits) + ']')