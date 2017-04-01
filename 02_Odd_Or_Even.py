#02 Odd Or Even

number = raw_input("Please enter a number: ")
number = int(number)

number2 = raw_input("Please enter a second number: ")
number2 = int(number2)

if number % number2 == 0:
	print(repr(number) + " is divisible by " + repr(number2))
else:
	print(repr(number) + " is not divisible by " + repr(number2))

#if number % 4 == 0:
#	print("Divisible by 4")
#else:
#	if number % 2 == 0:
#		print("Even Number")
#	else:
#		print("Odd Number")

