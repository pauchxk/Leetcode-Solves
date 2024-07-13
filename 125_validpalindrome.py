#Given a string s, return true if it is a palindrome, or false otherwise.#


def isPalindrome(s):
    new = ""
    for chr in s:
        if chr.isalnum() == False:
            s = s.replace(chr, "")
        else:
            new = chr.lower() + new
    if s.lower() == new:
        return True
    else:
        return False


#testing#
s = "Race car"
print(isPalindrome(s))
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = " "
print(isPalindrome(s))