l1 = True
l2 = False
l3 = True
l4 = True

s1 = bool(int(input('Input your condition: ')))
s2 = bool(int(input('Input your condition: ')))
s3 = bool(int(input('Input your condition: ')))

# s1 and s2 is on, l1 and l4 is on, the rest is flipped
# s2 and s3 is on, l2 and l4 is on, the rest is flipped
# s2 is on, l3 is on, the rest is flipped

if s1 == True and s2 == True and s3 == False:
    l1 = True
    l2 = not(l2)
    l3 = not(l3)
    l4 = True
elif s1 == False and s2 == True and s3 == True:
    l1 = not(l1)
    l2 = True
    l3 = not(l3)
    l4 = True
elif s1 == False and s2 == True and s3 == False:
    l1 = not(l1)
    l2 = not(l2)
    l3 = True
    l4 = not(l4)

print(l1)
print(l2)
print(l3)
print(l4)
