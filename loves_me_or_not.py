#loves_me_or_not.py

alpha = {'a': 1, 'b': 2,'c': 3, 'd': 4,'e': 5, 'f': 6,'g': 7, 'h': 8,'i': 9, 'j': 10,'k': 11, 'l': 12,'m': 13, 'n': 14,'o': 15, 'p': 16,'q': 17, 'r': 18,'s': 19, 't': 20,'u': 21, 'v': 22,'w': 23, 'x': 24,'y': 25, 'z': 26, ' ': 0}

#print alpha

name = raw_input("Please enter a name: ")
name = name.lower()
value = 0


for n in name:
	if n in alpha.keys():
		value = value + alpha[n]
		#print alpha[n]

#print value

if (value%2 == 1):
	print "(S)He loves you not"
elif (value%2 == 0):
	print "(S)He loves you, yeah, yeah, yeah"
else: #this should NEVER happen...
	print "You are unlovable... :("



