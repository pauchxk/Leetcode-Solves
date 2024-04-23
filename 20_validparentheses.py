#given a string s containing all types of brackets, determine if the input string is valid or not. return true or false respectively.

def isValid(s):
    stack = []
    opening = ['(','[','{']
    closing = [')',']','}']

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            else:
                top = stack.pop()
                if opening[closing.index(char)] != top:
                    return False
    if stack:
        return False
    
    return True


#testing#
s = "()"
print(isValid(s))
s = "()[]{}"
print(isValid(s))
s = "(]"
print(isValid(s))