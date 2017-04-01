#09 Guessing Game - 1

import random

guess = 0


while True:

	user_data = raw_input("Guess any number between 1 and 9: ")
	if user_data != "Exit":
		user_data = int(user_data)

	print ("Your Guess: " + repr(user_data))

	#Exit here
	if user_data == "Exit":
		break

	num = random.randint(1,9)

	print ("Random number: " + repr(num))

	if user_data == num:
		print("You Guessed Correctly!")
	elif num < user_data:
		print("The number you guessed was too high.")
	elif user_data > num:
		print("The Number you guessed was too low.")

	elif guess % 5 == 0:
		print("You can always exit by typing ""Exit""\n")

	guess += 1

if user_data == "Exit":
	print("You guessed " + repr(guess) + " times!")


