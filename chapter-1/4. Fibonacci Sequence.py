# Fibonacci Sequence
         
# Automatic memoization with decorator: @functools.lru_cache()

from functools import lru_cache

# maxsize defines the maximum number of entries in the cache
# maxsize=None means that the cache will grow indefinitely
@lru_cache(maxsize=None)
def fib4(n: int) -> int: # same definition of fib2()
    if n < 2:
        return n # base case
    
    return fib4(n - 2) + fib4(n - 1) # recursive case

if __name__ == "__main__":
    print(fib4(50))