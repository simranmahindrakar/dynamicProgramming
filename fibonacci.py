def fibonacci(n):
    if n==0 or n==1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    return (value)

print(fibonacci(5))
-------------------------------------------------------------------------------
//memoized fibo

def fibonacci(n):
    fibtable = {}
    if n in fibtable:
        return (fibtable[n])
    if n==0 or n==1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
        fibtable[n] = value
    return (value)

print(fibonacci(5))
----------------------------------------------------------------------
DP Fibo

class Solution:
    def fib(self, N: int) -> int:
        fibtable = {}
        fibtable [0]=0
        fibtable [1]=1
        for i in range(2,N+1):
            fibtable[i] = fibtable[i-1] + fibtable[i-2]
        return (fibtable[N])
