"""
Create a memoized fibonacci() function. This function should return the nth Fibonacci number.

Note: To avoid an infinite loop, either handle the edge case of negative numbers in your function, or do not call it using negative numbers.
"""

memo = {}


def fibonacci(n):
    answer = None
    if n < 0:
        raise ValueError("negative numbers are not supported")
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        answer = fibonacci(n-2) + fibonacci(n-1)
        memo[n] = answer
    return answer


# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))
