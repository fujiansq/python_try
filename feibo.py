def move(n,a,b):
	if a==0:
		print a,
	if n==1:
		print a+b,
	if n!=1:
		c=b
		b=a+b
		a=c
		print b,
		move(n-1,a,b)
		
move(10,0,1)