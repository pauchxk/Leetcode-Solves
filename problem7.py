#what is the 10001st prime number?

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False

    p = 2
    while p * p <=n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    
    prime_numbers = []
    for i in range(2, n+1):
        if primes[i]:
            prime_numbers.append(i)

    return prime_numbers


def find_nth_prime(n):
    prime_list = sieve_of_eratosthenes(110000)
    return prime_list[n-1]


print(find_nth_prime(10001))