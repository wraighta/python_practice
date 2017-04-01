#13 Fibonacci


i = raw_input("The nth fibonacci: ")
i = int(i)
print i


def fib(n):
	j=0
	n,m=1,1
	for j in range(n-1):
		n,m = m, n+m
		print n
		print m
		return n

print fib(i)


	




