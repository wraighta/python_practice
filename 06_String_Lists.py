#06 String Lists

string = raw_input("Is this word a palidrome? ")
string2 = []
i=1
a=0

#print string
#print len(string)

#for i in range(0,len(string)):
#	print repr(len(string)-i)


for s in string:
	string2.append(string[len(string)-i])
	#print s
	i+=1
	#print string2
	
#print string2

for j in range(0,len(string)):
	#print (string[j] + " AND " + string2[j])
	if string[j] != string2[j]:
		print "This word is not a palindrome."
		break
	else:
		a+=1

if a == len(string):
	print "This word is a palindrome."






