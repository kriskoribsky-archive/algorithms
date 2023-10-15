# Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0

for i in range(0, 1000, 3):
    total += i

for j in range(0, 1000, 5):
    if j%3 != 0:
        total += j

print(total)
