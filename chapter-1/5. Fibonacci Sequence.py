# Fibonacci Sequence

# Applying traditional iterative

def fib5(n: int) -> int:
    if n == 0: return n # special case

    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)

    # Tuple unpacking
    # This foor loop will be excuted n - 1 times
    for _ in range(1, n):
        last, next = next, last + next

    return next

if __name__ == "__main__":
    print(fib5(5))