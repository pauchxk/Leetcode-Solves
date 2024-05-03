#Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largestPalindrome():
    largest_palindrome = 0

    for i in range(100,999):
        for j in range(100,999):
            product = i * j

            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

print(largestPalindrome())