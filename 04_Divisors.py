#04 Divisors

num = raw_input("Input number: ")
num = int(num)

x=range(2,num)

for elem in x:
	if num % elem == 0:
		print(repr(num) + " goes into " + repr(elem))


