#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 1, Exercise 6

def isint(string):
	try:
		int(string)
		return True
	except:
		return False

def prime_factor(number):
    factors = []
    i = 2
    factorized_number = number
    while i * i <= number:
        if factorized_number % i != 0:
            i += 1
        else:
            factors.append(i)
            factorized_number = factorized_number // i
    return factors

def factor_counter(numlist):
    new_fac = []
    count = []
    for i in numlist:
        if i not in new_fac:
            count.append(numlist.count(i))
            new_fac.append(i)
    power_list = [new_fac, count]
    return power_list

while True:
    print('Enter a number. Type STOP to break.')
    num = input()
    if num.casefold() == 'stop':
        break
    elif isint(num) == True:
        power = factor_counter(prime_factor(int(num)))
        print('Your number ' + num + ' is divisible by:')
        for n in range(0, len(power[0])):
            print(str(power[0][n]) + ' to the power of ' + str(power[1][n]))
    else:
        print('Not a number. Enter a number. Type STOP to break.')