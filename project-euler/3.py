# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math


def largest_prime(num):
    # the key to this problem is to perform decomposition into prime numbers
    # that is, to evenly divide the given number with ascending prime numbers until the result of division by prime number will be another prime number
    # this prime number will also be the highest prime factor of the given number

    while num > 1:
        for i in range(2, math.ceil((num**(1/2)))+1):
            if num % i == 0:
                num /= i
                break
        else:
            return int(num)
    else:
        return 1


print(largest_prime(600851475143))
