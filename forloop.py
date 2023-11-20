inp = input()
inp2 = input()

inp = inp.split(',')
found = False
i=0

for i in range(len(inp)):
        i <= len(inp2)
        if inp2==inp[i]:
            found = True
            print(i)
        i+=1
# if i!=x:
#     print('not found')
if not found:
    print("not found")
