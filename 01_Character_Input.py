#01 Character Input

i=1

name = raw_input("Give me your name: ")
print("Your name is " + name)

age = raw_input("Enter your age: ")
age = int(age)

print(name + ", You will be 100 years old in the year " + repr(2016+(100-age)) )

repeat = raw_input("How many times would you like to repeat the results? ")
repeat = int(repeat)

for i in range(repeat):
	print(name + ", You will be 100 years old in the year " + repr(2016+(100-age)) )
	i=i+1
