""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"

    def run_cycle(n):
        def func(x):
            f = x
            m = 1
            while m <=n:

                if m % 3 == 1:
                    f = f1(f)
                elif m % 3 ==2:
                    f = f2(f)
                else:
                    f = f3(f)
                m += 1
            return f
        return func
    return run_cycle




## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: 10*y + x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def check(i):
        if i == 1:
            return True
        elif n % i == 0:
            return False

        else:
            return check(i-1)
    return check(n-1)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def sum():
        sum1 = 0
        sum2 = 0
        def sum_odd(a, sum1):
            if a == n:
                sum1 += odd_term(a)
                return sum1
            elif a > n:
                return sum1
            else:
                sum1 += odd_term(a)
                return sum_odd(a+2,sum1)
        def sum_even(a,sum2):
            if a == n:
                sum2 += even_term(a)
                return sum2
            elif a > n:
                return sum2
            else:
                sum2 += even_term(a)
                return sum_even(a+2, sum2)
        return sum_odd(1,sum1) + sum_even(2,sum2)
    return sum()
    '''或者：'''
    def helper(term0, term1, k):
        if k == n:
            return term0(k)
        return term0(k) + helper(term1, term0, k + 1)
    return helper(odd_term, even_term, 1)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count(n//10, 10-n%10)

    def count(n,digit):
        if n == 0:
            return 0
        elif n % 10 == digit:
            return count(n//10,10-n%10) + 1
        else:
            return count(n//10,10-n%10) + 1
