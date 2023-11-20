# Recursive Binary COnverter

    # I want the number to be fleksible
binNum = int(input("Input your binary number: "))
    
# Recursion
def count(binNum):
    # Base Case
    if (binNum == 0):
        return 
    # Recursive Case
    else:
        # we call again the function
        count(int(binNum/2))
        print(binNum%2, end= " ")

count(binNum)
