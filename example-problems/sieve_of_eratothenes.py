"""
The sieve provides a set of steps for finding all prime numbers up to a given limit.

The sieve works by first assuming that all numbers from {2,…,n} are prime, and then successively marking them as NOT prime.

The algorithm works as follows:

1. Create a list of all integers from 2 to n.
    - since using indices to represent the actual number, we will start the array from 0 and essentially ignore the values of array[0] and array[1].
2. Start with the smallest number in the list (2, the smallest prime number).
3. Mark all multiples of that number up to n as not prime.
4. Move to the next non-marked number and repeat this process until the entire list has been covered.

When the steps are complete, all remaining non-marked numbers are prime.
"""


# import math library
import math


def sieve_of_eratosthenes(limit):
    # handle edge cases
    if (limit <= 1):
        return []

    # create the output list
    output = [True] * (limit+1)

    # mark 0 and 1 as non-prime
    output[0] = False
    output[1] = False

    # iterate up to the square root of the limit
    for i in range(2, math.floor(math.sqrt(limit))):
        if (output[i] == True):
            j = i ** 2    # initialize j to square of i

            # mark all multiples of i as non-prime
            while j <= limit:
                output[j] = False
                j += i

    # remove non-prime numbers
    output_with_indices = list(enumerate(output))
    trues = [index for (index, value) in output_with_indices if value == True]
    return trues


primes = sieve_of_eratosthenes(20)
print(primes)  # return [2, 3, 5, 7, 11, 13, 17, 19]
