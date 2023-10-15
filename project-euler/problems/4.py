# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# function for calculating the largest palindrome of 2 x-digit numbers
def largest_palindrome(digits):

    # largest possible non-palindromic product of x-digit numbers
    m = str(int("9"*digits)**2)

    # since the digits of 2 numbers will be the same length, their largest palindrome will always be an integer with even number of digits
    # now, we just need to iterate over palindromes in descening order and the biggest product

    left_m = int(m[:int(len(m)/2)])

    if str(left_m) == m[int(len(m)/2):]:
        return int(m)
    else:
        left_m -= 1

    while left_m > 1:

        pl = f = int(str(left_m)+str(left_m)[::-1])

        while len(str(f)) > digits:
            for i in range(int(f**(1/2)), 1, -1):
                if f % i == 0:
                    f //= i
                    break
            else:
                break
        else:
            if len(str(pl//f)) == digits:
                return pl

        left_m -= 1

    else:
        return 1


print(largest_palindrome(3))
