"""
Thiss code defines a function is_prime that checks
if a number n is prime. It returns True and False otherwise.
The function uses a loop to check for factors up to the square 
root of n, which makes it more efficient.
square root of n is efficient because if n is not a prime number,
it can be factored into two factors, a and b, such that n = a * b.
If both a and b were greater than the square root of n, then a * b
would be greater than n, which is a contradiction. Therefore, 
at least one of the factors must be less than or equal to the
square root of n.
By only checking for factors up to the square root of n, you 
reduce the number of checks needed, making the algorithm more
efficient. This significantly cuts down the number of iterations,
especially for large numbers.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = 75
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")