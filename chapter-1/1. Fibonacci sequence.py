# Fibonacci Sequence

# The sum of two numbers is the next number in the sequence
# Except the first two numbers. They are 0 and 1
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21...

# Formula
# fib(n) = fib(n - 1) + fib(n - 2)

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(5))

# ERROR: RecursionError: maximum recursion depth exceeded

# Example of infinity recursion
# def f():
#     f() + f()
