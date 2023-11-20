def recur_fib(n):
    if (n == 1):
        return 1
    elif (n == 0):
        return 0
    else:
        return (recur_fib(n-1) + recur_fib(n-2))
    
n = int(input('number: '))
for i in range(n):
    print(recur_fib(i), end=" ")
