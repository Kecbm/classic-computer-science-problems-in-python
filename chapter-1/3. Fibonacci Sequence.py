# Fibonacci Sequence

# Applying memoization
# It is to be used the memory to store the results of the function calls
# Example:
# 👩🏾 - Do you know n?
# 🖥️ - I know n (consulting n im my memory)
# 🖥️ - I know n (calculate n)

# We appliyng memoization with a dictionary

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # our base case

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)

    return memo[n]

# ow, we can execute fib3(50) without any problem

if __name__ == "__main__":
    print(fib3(50))

# one call of fib3(20) results in 39 executions of fib3(20)
# one call of fib3(20) results in 21.891 executions of fib3(20) 🔥
