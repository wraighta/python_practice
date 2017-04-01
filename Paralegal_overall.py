import string

file = open('C:/Python27/Paralegal Marks Overall.txt', 'r+')


line=''
course = [''] 
mark =[0] 
i=0



for line in file.readlines():
	#zfile.readline()
	#line[-4:-1] len(line)
	#if line.isdigit():
	#print line
	course.append('')
	course[i] = line
	i+=1
	
#print i

for ii in range (0,i-1):
	mark.append(0)
	

for j in range(0, i): 
	#print course[j]
	#print len(course[j])
	#print course[j][(len(course[j])-3):(len(course[j])-1)]
	mark[j] = (int(course[j][(len(course[j])-3):(len(course[j])-1)]))
	#print mark[j]


def avg(grades):
	a=0
	x=len(grades)	

	for k in range(0,x):
		a=a+grades[k]

	#print a
	#print a/x
	print "Average calculated"
	return a/x
	
	

#print avg(mark)

file2 = open("C:/Python27/Overall Average.txt", "w")

#file2.seek(0,2)

file2.write('Your current average in the Paralegal Program is '+repr(avg(mark))+'%')

#file.write('\nYour current average in the Paralegal Program is '+repr(avg(mark))+'%')

file2.close	
file.close

