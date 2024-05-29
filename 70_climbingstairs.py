#you are climbing a staircase; it takes n steps to reach
#the top. each time you can either climb one or two steps.
#in how many distinct ways can you climb to the top?

#solution: using the fibonacci sequence#
def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    
    a, b = 1,1

    for _ in range(2, n+1):
        a, b = b, a + b

    return b


#testing#
n = 5
print(climb_stairs(n))