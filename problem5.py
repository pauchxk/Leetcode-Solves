#what is the smallest positive number that is evenly divisible 
#by all of the numbers from 1 to 20?

def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def compute_lcm(numbers):
    all_factors = {}

    for num in numbers:
        factors = prime_factors(num)

        for factor in set(factors):
            count = factors.count(factor)

            if factor not in all_factors or all_factors[factor] < count:
                all_factors[factor] = count
    
    lcm = 1
    for factor, count in all_factors.items():
        lcm *= factor ** count

    return lcm

def smallest_multiple():
    numbers = list(range(1, 21))
    return compute_lcm(numbers)

print(smallest_multiple())