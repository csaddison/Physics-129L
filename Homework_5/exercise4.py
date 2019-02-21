#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 5, Exercise 4

# Gets input and converts to binary if input is a reasonably sized integer
print('Enter an integer less than 65535:')
num = input()
while True:
    try:
        num = int(num)
        if num > 65535:
            print("Number too large to decode")
            break
        bnum = format(int(num), '016b')
    except:
        print("Not an integer")
        break

    # Converting to string to slice
    bnum = str(bnum)

    # Slicing the 16bit number and decoding each into base 10
    channel = int(bnum[-4:], 2)
    time = int(bnum[-8:-4], 2)
    height = int(bnum[:-8], 2)

    # Printing final message
    print('You are on channel ' + str(channel) + '. You are recording a pulseheight of ' + str(height) + 'um over a time ' + str(time) + 'ms.')
    break
