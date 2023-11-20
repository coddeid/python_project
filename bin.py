# Binary Converter
# input and indexing
def binary():
    num = input("Input your binary number: ")
    l = list(num)
    rs = 0
# Reverse the list so that we can get
# index 0, 1, 2, 3 based on binary
    rev = l[::-1]
    print((rev))

# Count
    for i in range(len(rev)):
        rs += rs + int(rev[i])*2**i
    print(rs)

# Command

# def option():
#     y = 1
#     n = 0
#     option = input("Would you like to continue?y/n ")
#     while option != 0:
#         if option == 1:
#             # Call the function
#             print(binary())
#             return
        
binary()
# option()
