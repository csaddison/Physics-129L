#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 1, Exercise 4

for i in range(100,401):
    number = str(i)
    even = True
    for digit in number:
        if int(digit) % 2 != 0:
            even = False
    if even == True:
        print(number)