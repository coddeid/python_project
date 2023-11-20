# input1=int(input("input: "))

# x0=0
# x1=1


# for x in range(input1):
#         x2=x0+x1
#         x0=x1
#         x1=x2
# print("output:", x0)

fib = int(input())

x0 = 0
x1 = 1

if fib >= 1:
    for fib in range(fib):
        x2=x1+x0
        x0=x1
        x1=x2

        print(x1, end=" ")
else:
    print('invalid')
