#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 1, Exercise 1

def isint(string):
	try:
		int(string)
		return True
	except:
		return False
        
def isfloat(string):
	try:
		float(string)
		return True
	except:
		return False

while True:
	print("Enter an integer number: ")
	num = input()
	if isint(num) == True:
		print("Your number squared is " + str(int(num)**2))
		break
	elif isfloat(num) == True:
		print("You didn't give an integer. Your nearest number squared is " + str(round(float(num))**2))
		break
	elif num.casefold() == 'stop':
		break
	else:
		print("That's not an acceptable input. Enter an integer number--no letters. Type STOP to break.")