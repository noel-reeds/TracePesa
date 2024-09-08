#!/usr/bin/env python3

def fib(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]

print(fib(10))
