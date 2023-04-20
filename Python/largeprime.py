number = int(input())

def get_prime_factors(n):
    divisble = 2
    prime_factors = []
    while n > 1:
        if n % divisble == 0:
            prime_factors.append(divisble)
            n = n // divisble
        else:
            divisble += 1
    return prime_factors

prime_factors = get_prime_factors(number)
print(prime_factors)