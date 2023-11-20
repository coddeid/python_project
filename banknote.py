# take user input the total amount of the money
amount = int(input())

# initialize for all notes equals to 0
note500 = note100 = note50 = note20 = note10 = note5 = note2 = note1 = 0

# Calculate the notes
if amount <= 9999999 :
    note500 = int(amount / 500)
    rem = amount % 500

    note100 = rem / 100
    rem %= 100

    note50 = rem / 50
    rem %= 50

    note20 = rem / 20
    rem %= 20

    note10 = rem / 10
    rem %= 10

    note5 = rem / 5
    rem %= 5 

    note2 = rem / 2
    rem %= 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 499 :
    note100 = int(amount / 100)
    rem = amount % 100

    note50 = rem / 50
    rem %= 50

    note20 = rem / 20
    rem %= 20

    note10 = rem / 10
    rem %= 10

    note5 = rem / 5
    rem %= 5 

    note2 = rem / 2
    rem %= 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 99 :
    note50 = int(amount / 50)
    rem = amount % 50

    note20 = rem / 20
    rem %= 20

    note10 = rem / 10
    rem %= 10

    note5 = rem / 5
    rem %= 5 

    note2 = rem / 2
    rem %= 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 49 :
    note20 = int(amount / 20)
    rem = amount % 20

    note10 = rem / 10
    rem %= 10

    note5 = rem / 5
    rem %= 5 

    note2 = rem / 2
    rem %= 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 19 :
    note10 = int(amount / 10) 
    rem = amount % 10

    note5 = rem / 5
    rem %= 5 

    note2 = rem / 2
    rem %= 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 9:
    note5 = int(amount / 5)
    rem = amount % 5

    note2 = rem / 2
    rem %= 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 4 :
    note2 = int(amount / 2)
    rem = amount % 2

    note1 = rem / 1 
    rem %= 1

elif amount <= 1:
    note1 = int(amount / 1) 
    rem = amount % 1

else:
    note500 = note100 = note50 = note20 = note10 = note5 = note2 = note1 = 0



# Print the result
print(f"500 = {int(note500)}")
print(f"100 = {int(note100)}")
print(f"50 = {int(note50)}")
print(f"20 = {int(note20)}")
print(f"10 = {int(note10)}")
print(f"5 = {int(note5)}")
print(f"2 = {int(note2)}")
print(f"1 = {int(note1)}")
