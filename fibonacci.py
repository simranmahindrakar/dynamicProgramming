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
