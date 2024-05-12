#return the square root of x rounded down to the nearest integer WITHOUT using any built-in exponents or functions.

#first solution: binary search
# def calc_sqrt(x):
#     if x == 0 or x == 1:
#         return x

#     left, right = 1, x
#     result = 0

#     while left <= right:
#         mid = (left + right) // 2

#         if mid * mid == x:
#             return mid

#         elif mid * mid < x:
#             left = mid + 1
#             result = mid

#         else:
#             right = mid - 1

#     return result


#alternative solution: newton's method
def calc_sqrt(x):

    b = x

    while b*b > x: b=(b+x//b)//2

    return b


#testing#
x = 8
print(calc_sqrt(x))