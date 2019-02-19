#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 4

print('Enter an integer:')
num = input()
try:
    b_num = str(bin(int(num)))
except:
    "Not an integer"
print(b_num)