# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math


# prime numbers in 1-20: 2, 3, 5, 7, 11, 13, 17, 19


# searched number
# x = 1

# multiply by all prime numbers in range 1-20 since if number is divisible by any of the prime numbers, they must be included in the   numbers's prime factorization

# x *= 2 * 5 * 7 * 11 * 13 * 17 * 19


def prime_search(int_range):

    prime = []

    # calculate all prime numbers in range
    for x in int_range:

        # square root of given number is a max value that can be a prime number
        for i in range(2, math.isqrt(x)+1):
            if x % i == 0:
                break

        else:
            prime.append(x)

    return prime


def prime_factorization(num):

    # create dictionary in form prime_number/base : exponent
    factors = dict()

    while num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                factors.update({i: (factors.get(i) or 0)+1})

                num //= i
                break

    return factors


def smallest_multiple(max_factor):

    int_range = range(2, max_factor+1)

    # create dict of factors and exponents of searched number x
    x_factors = dict.fromkeys(int_range, 0)

    prime = prime_search(int_range)

    # subtract set of prime numbers from default set to get composite numbers
    composite = [x for x in int_range if x not in prime]

    # add primes to factorization
    for p in prime:
        x_factors[p] = 1

    # add composite numbers prime factors to factorization (basically mathematical unification of sets)
    for c in composite:
        c = prime_factorization(c)

        for f in c.keys():
            if c.get(f) > x_factors.get(f):
                x_factors[f] = c.get(f)

    return math.prod(x**x_factors.get(x) for x in x_factors.keys())


print(smallest_multiple(20000000))
