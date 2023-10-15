import sys
import time



# PERMUTATIONS WITHOUT REPETITION
# 16.10.2021
# Kristián Koribský

# math source: https://www.mathsisfun.com/combinatorics/combinations-permutations.html

def permutations_without_repetition(n, r, permutations=[], subset=[]):

    # ALGORITHM DESCRIPTION
    # this algorithm is recursively called starting with a single element and up to r elements
    # it recursively iterates over all possible permutations without repetition
    # when algorithm reaches length of a single possible subset that is equal to r,
    # it adds this subset to all permutations and the tree terminates adding subset to permutations, therefore
    # it is similiar to recursively accessing tree branches

    # IMPORTANT
    # this algorithm won't check for duplicates in the input array due to the improvement of performance
    # please make sure to not include array with duplicates as this is permutations without repetition

    # useful print statements for debug/algorithm explanation
    # print(f"running function with n:{n}, len(subset):{len(subset)}, r:{r}, subset:{subset}, permutations:{permutations}")

    # print(f"running function: n before edit={n}", end="     ")

    # n = [x for x in n if x not in subset]

    # print(f"n after edit={n}, subset={subset}")

    if len(subset) == r:
        permutations.extend([subset])
        # returning permutation just because of the case where r = 0 in the input, else just return would be sufficient
        return permutations

    n = [x for x in n if x not in subset]

    for x in n:
        permutations_without_repetition(n, r, permutations, subset+[x])

    return permutations


# return factorial of a given number
def factorial(number):

    fact = 1

    for i in range(1, number+1):
        fact *= i

    return fact


print("\nThis program calculates all possible permutations without repetition in a given set (without duplicate values).")
print("Permutations without repetition, the order of the elemets matters.")
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

print("mathematical formula: n! / (n-r)!")

permutations = factorial(len(n)) // factorial(len(n)-r)

print(f"permutations: {permutations}")


print("---------------------------------------------------------------------------------------------------------------")
print("RESULT")
result = permutations_without_repetition(n, r)
print(f"\n{result}")
print(f"\nnumber of pairs = {len(result)}")

print("\n---------------------------------------------------------------------------------------------------------------")
print("PERMUTATIONS WITHOUT REPETITION\n16.10.2021\nKristián Koribský\n")