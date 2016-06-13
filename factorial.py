Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fact():
	i=5
	x=1
	if i>1:
		for j in range(i+1):
			x*=j
		print (x)
	else:
		print(None)

		
>>> print (fact())
0
None
>>> def fact():
	i=5
	x=1
	if i>1:
		for j in range(1,i+1):
			x*=j
		print (x)
	else:
		print(None)

		
>>> print(fact())
120
None
>>> def fact():
	i=5
	x=1
	if i>1:
		for j in range(1,i+1):
			x*=j
		print (x)
	else:
		print(None)

>>> print(fact())
120
None
>>> def fact():
	i=5
	x=1
	if i>1:
		for j in range(1,i+1):
			x*=j
		print (x)

	
>>> print(fact())
120
None
>>> def fact():
	i=5
	x=1
	if i<0:
		print("no fact for negatives")
	elif i==0:
		print("fact for zero is 1")
	else:
		for j in range(1,i+1):
			x*=j
		print (x)

	
>>> print(fact())
120
None
>>> def fact():
	i=5
	x=1
	if i<0:
		print("no fact for negatives")
	elif i==0:
		print("fact for zero is 1")
	else:
		for j in range(1,i+1):
			x*=j
		return (x)

	
>>> print(fact())
120
>>> def fact(x):
	if x<0:
		return "No fact for negatives"
	elif x==0:
		return 1
	else:
		return x*fact(x-1)

	
>>> print fact(4)
SyntaxError: invalid syntax
>>> print(fact(4))
24
>>> print (fact(0))
1
>>> import math
>>> math.factorial (0)
1
>>> math.factorial (1)
1
>>> fact(1)
1
>>> fact(0)
1
>>> fact()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    fact()
TypeError: fact() missing 1 required positional argument: 'x'
>>> 
