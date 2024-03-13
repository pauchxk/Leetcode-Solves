#Given a positive integer n, find the pivot integer x such that:
#The sum of all elements between 1 and x inclusively equals the sum of all elements 
#between x and n inclusively. Return the pivot integer x. If no such integer 
#exists, return -1. It is guaranteed that there will be at 
#most one pivot index for the given input.

n = 8

from math import sqrt
x = sqrt(n * (n + 1) / 2)
if x % 1 != 0:
    print(-1)
else:
    print(int(x))

#OR:
li, c = [i for i in range(1, n+1)], -1
for i in range(len(li)):
    if sum(li[0:i+1]) == sum(li[i:]):
        c = i + 1
print(c)

#OR:
for i in range(1, n + 1):
    sum_left = sum(range(1, i + 1))
    sum_right = sum(range(i, n + 1))
    if sum_left == sum_right:
        print(i)
print(-1)