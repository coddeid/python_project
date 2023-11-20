# separated the input
class Number:
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j

# SUM the input and then divide by 10
def count(x1):
    num1 = x1.a + x1.b + x1.c + x1.d + x1.e + x1.f + x1.g + x1.h + x1.i + x1.j

    num2 = 10
    return(num1/num2)

# Input the number and change the input into INTEGER
x1 = Number(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()))

print(f"The average is equal to {count(x1)}")
