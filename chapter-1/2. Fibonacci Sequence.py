# Fibonacci Sequence

# Applying the base case: the first two numbers are 0 and 1
# The sum for this numbers is forever 2

def fib2(n : int) -> int:
    if n < 2: # base case
        return n
    
    return fib2(n - 2) + fib2(n - 1) # recursive case

if __name__ == "__main__":
    print(fib2(5))

# Every execution of fib2() results in two more executions of fib2()
# Will get a infinity execution for fib2(50)
