#What is the largest prime factor of the number 600851475143?
def largest_prime_factor():

    n = 600851475143

    largest_prime = 0

    while n % 2 == 0:
        largest_prime = i
        n //= i

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //=i

    if n > 2:
        largest_prime = n

    return largest_prime

print(largest_prime_factor())