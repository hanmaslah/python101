Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def prime(n):
	if n>1:
		for i in range (2,n):
			if n%i==0:
				print (n, "is not prime")
				print(i, "times", n//i, "is", n)
				break
			else:
				print(n, "is prime")

				
>>> print (prime(10))
10 is not prime
2 times 5 is 10
None
>>> def prime(n):
	if n>1:
		for i in range (2,n):
			if n%i==0:
				print (n, "is not prime")
				print(i, "times", n//i, "is", n)
				break
			else:
				print(n, "is prime")
		prime(n-1)

		
>>> print(prime(10))
10 is not prime
2 times 5 is 10
9 is prime
9 is not prime
3 times 3 is 9
8 is not prime
2 times 4 is 8
7 is prime
7 is prime
7 is prime
7 is prime
7 is prime
6 is not prime
2 times 3 is 6
5 is prime
5 is prime
5 is prime
4 is not prime
2 times 2 is 4
3 is prime
None
>>> def prime(n):
	if n>1:
		for i in range (2,n):
			if n%i==0:
				print (n, "is not prime")
				print(i, "times", n//i, "is", n)
				break
			else:
				print(n, "is prime")
				break
		prime(n-1)

>>> print (prime(10))
10 is not prime
2 times 5 is 10
9 is prime
8 is not prime
2 times 4 is 8
7 is prime
6 is not prime
2 times 3 is 6
5 is prime
4 is not prime
2 times 2 is 4
3 is prime
None
>>> def prime(n):
	if n>1:
		for i in range (2,n):
			if n%i==0:
				print (n, "is not prime")
				print(i, "times", n//i, "is", n)
				break
			else:
				print(n, "is prime")
		        prime(n-1)
		        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> if n>1:
		for i in range (2,n):
			if n%i==0:
				return (n, "is not prime")
				print(i, "times", n//i, "is", n)
				break
			else:
				return(n, "is prime")
		prime(n-1)
		
SyntaxError: 'return' outside function
>>> def prime(n):
	if n>1:
		for i in range (2,n):
			if n%i==0:
				
				return(i, "times", n//i, "is", n)
				return (n, "is not prime")
				break
			else:
				return(n, "is prime")
		prime(n-1)

		
>>> print(prime(10))
(2, 'times', 5, 'is', 10)
>>> def prime(n):
	
		for i in range (2,n):
			if n>1:
				for i in range (2,n):
					if n%i==0:
						print (n, "is not prime")
						print(i, "times", n//i, "is", n)
						break
					else:
						print(n, "is prime")

	
>>> print(prime(10))
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
10 is not prime
2 times 5 is 10
None
>>> def prime(k):
	
		for n in range (2,k):
			if k>1:
				for i in range (2,n):
					if n%i==0:
						print (n, "is not prime")
						print(i, "times", n//i, "is", n)
						break
					else:
						print(n, "is prime")

						
>>> print(prime(10))
3 is prime
4 is not prime
2 times 2 is 4
5 is prime
5 is prime
5 is prime
6 is not prime
2 times 3 is 6
7 is prime
7 is prime
7 is prime
7 is prime
7 is prime
8 is not prime
2 times 4 is 8
9 is prime
9 is not prime
3 times 3 is 9
None
>>> def prime(k):
	
		for n in range (2,k):
			if k>1:
				for i in range (2,n):
					if n%i==0:
						
						break
					else:
						print(n, "is prime")

						
>>> print(prime(10))
3 is prime
5 is prime
5 is prime
5 is prime
7 is prime
7 is prime
7 is prime
7 is prime
7 is prime
9 is prime
None
>>> def prime(k):
	
		for n in range (2,k):
			if k>1:
				for i in range (2,n):
					if n%i==0:
						print (n, "is not prime")
						print(i, "times", n//i, "is", n)
						break
				else:
					print(n, "is prime")

					
>>> print(prime(10))
2 is prime
3 is prime
4 is not prime
2 times 2 is 4
5 is prime
6 is not prime
2 times 3 is 6
7 is prime
8 is not prime
2 times 4 is 8
9 is not prime
3 times 3 is 9
None
>>> def prime(k):
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not prime")
				break
		else:
			print(n, "is prime")
	prime(k-1)

	
>>> print(prime(10))
10 is not prime
9 is not prime
8 is not prime
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(prime(10))
  File "<pyshell#41>", line 9, in prime
    prime(k-1)
  File "<pyshell#41>", line 9, in prime
    prime(k-1)
  File "<pyshell#41>", line 9, in prime
    prime(k-1)
  File "<pyshell#41>", line 8, in prime
    print(n, "is prime")
NameError: name 'n' is not defined
>>> def prime(k):
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not prime")
				break
		else:
			print(k, "is prime")
	prime(k-1)

	
>>> print(prime(10))
10 is not prime
9 is not prime
8 is not prime
7 is prime
6 is not prime
5 is prime
4 is not prime
3 is prime
2 is prime
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(prime(10))
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 9, in prime
    prime(k-1)
  File "<pyshell#44>", line 2, in prime
    if k>1:
RecursionError: maximum recursion depth exceeded in comparison
>>> def prime(k):
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not prime")
				break
		else:
			print(n, "is prime")
	else:
		return k, "is not prime"
	prime(k-1)

	
>>> print(prime(10))
10 is not prime
9 is not prime
8 is not prime
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(prime(10))
  File "<pyshell#47>", line 11, in prime
    prime(k-1)
  File "<pyshell#47>", line 11, in prime
    prime(k-1)
  File "<pyshell#47>", line 11, in prime
    prime(k-1)
  File "<pyshell#47>", line 8, in prime
    print(n, "is prime")
NameError: name 'n' is not defined
>>> def prime(k):
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not prime")
				break
		else:
			print(k, "is prime")
	else:
		return k, "is not prime"
	prime(k-1)

	
>>> print(prime(10))
10 is not prime
9 is not prime
8 is not prime
7 is prime
6 is not prime
5 is prime
4 is not prime
3 is prime
2 is prime
None
>>> def prime(k):
	if k>1:
		for i in range(2,k):
			if k%i==0:
				print(k, "is not prime")
				break
		else:
			print(k, "is prime")
	else:
		return None 
	prime(k-1)

	
>>> print (prime (10))
10 is not prime
9 is not prime
8 is not prime
7 is prime
6 is not prime
5 is prime
4 is not prime
3 is prime
2 is prime
None
>>> print (prime(1))
None
>>> 
