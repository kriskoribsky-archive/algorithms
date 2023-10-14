import sys
import time



# COMBINATIONS WITHOUT REPETITION
# 16.10.2021
# Kristián Koribský

# math source: https://www.mathsisfun.com/combinatorics/combinations-permutations.html

def combinations_without_repetition(n, r):

    def permutations_without_repetition(n, r, permutations=[], subset=[]):

        # ALGORITHM DESCRIPTION
        # this algorithm is more thoroughly explained in "permutations without repetition.py" file in algorithms folder

        if len(subset) == r:
            permutations.extend([subset])
            return permutations

        n = [x for x in n if x not in subset]

        for x in n:
            permutations_without_repetition(n, r, permutations, subset+[x])

        return permutations


    # ALGORITHM DESCRIPTION
    # this one is pretty straightforward
    # firstly, use previous algorithm for calculating permutations without repetition
    # and then, since combinations are the same as permutations but order doesn't matter,
    # so there will be less pairs in combinations, just remove pairs in permutations with the same valeus to get combinations

    permutations = permutations_without_repetition(n, r)

    # exclusion of the same values (but with different variations) will be done by ordering them
    # if the 2 variants are contain same values, don't include into combinations

    combinations_ordered = []
    combinations = []

    for x in permutations:

        x_sorted = sorted(x)

        if x_sorted not in combinations_ordered:

            combinations.append(x)
            combinations_ordered.append(x_sorted)

    return combinations

    

# return factorial of a given number
def factorial(number):

    fact = 1

    for i in range(1, number+1):
        fact *= i

    return fact


print("\nThis program calculates all possible combinations without repetition in a given set (without duplicate values).")
print("combinations without repetition, the order of the elemets doesn't matter.")
print("---------------------------------------------------------------------------------------------------------------")
print("INPUTS")

tries = 5

while tries:
    try:
        raw_n = input("Enter set (n): ")
        # remove any type of leading/trailing parenthesis
        raw_n = raw_n.strip("[](){}<>")

        # remove , in between set elements
        raw_n = raw_n.replace(",", " ")

        # remove all the possible spaces in between the values, convert to int and remove duplicates (set)
        n = set(map(lambda x: int(str(x).strip()), raw_n.split()))

        r = int(input("Enter pairs count (r): "))

        assert r <= len(n)

    except AssertionError:
        print("r must be less than or equal to n, please try again")
        time.sleep(2)

    # except:
    #     print("Wrong input format, please try again")
    #     time.sleep(2)

    # The advantage of except Exception over the bare except is that there are a few exceptions that it wont catch,
    # most obviously KeyboardInterrupt and SystemExit: if you caught and swallowed those then you could make it hard for anyone to exit your script.
    # https://stackoverflow.com/questions/4990718/how-can-i-write-a-try-except-block-that-catches-all-exceptions
    # https://docs.python.org/2/library/exceptions.html#exceptions.Exception
    except Exception as e:
        print(f"{e} occurred while processing inputs, please try again")
        time.sleep(2)

    else:
        print("---------------------------------------------------------------------------------------------------------------")
        print("INPUTS VALID")
        print(f"set: {n}")
        print(f"length of set: {len(n)}")
        print(f"r: {r}")
        break

    finally:
        tries -= 1

else:
    print("\nYou have run out of input tries, closing the program.")

    # https://stackoverflow.com/questions/73663/how-to-terminate-a-script
    sys.exit()

print("---------------------------------------------------------------------------------------------------------------")
print("BEGINNING CALCULATION")

print("mathematical formula: n! / (r!(n-r)!)")

combinations = factorial(len(n)) // (factorial(r)*factorial(len(n)-r))

print(f"combinations: {combinations}")


print("---------------------------------------------------------------------------------------------------------------")
print("RESULT")

result = combinations_without_repetition(n, r)

print(f"\n{result}")
print(f"\nnumber of pairs = {len(result)}")

print("\n---------------------------------------------------------------------------------------------------------------")
print("COMBINATIONS WITHOUT REPETITION\n16.10.2021\nKristián Koribský\n")
