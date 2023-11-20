bin = int(input("Input your binary number: "))

num, i = 0, 0

# Looping
while bin>0:
    # If we see the binary pattern, it's multiple by 10
    mod = bin%10 
    x = mod*(pow(2,i))
    num += x
    bin //= 10
    i += 1

print("Result: ", num)
