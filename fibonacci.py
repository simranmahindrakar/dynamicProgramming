def fibonacci(n):
    if n==0 or n==1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    return (value)

print(fibonacci(5))
