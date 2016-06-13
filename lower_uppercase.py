Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def least_fact(x):
	for i in range(2,x+1):
		if x%i==0:
			return i

		
>>> least_fact (49)
7
>>> least_fact (81)
3
>>> 32768
32768
>>> least_fact (32768)
2
>>> z=81
>>> least_fact (z)*z
243
>>> def conv(x):
	l=[]
	for c in x.strip():
		if c.islower():
			l.append(c.upper)
		elif c.isupper():
			l.append(c.lower)
	print(str(l).strip('[]'))

	
>>> conv('Hello')
<built-in method lower of str object at 0x0000001244550148>, <built-in method upper of str object at 0x0000001244235E68>, <built-in method upper of str object at 0x0000001244337148>, <built-in method upper of str object at 0x0000001244337148>, <built-in method upper of str object at 0x0000001244235FB8>
>>> print (conv('Hello'))
<built-in method lower of str object at 0x0000001244550148>, <built-in method upper of str object at 0x0000001244235E68>, <built-in method upper of str object at 0x0000001244337148>, <built-in method upper of str object at 0x0000001244337148>, <built-in method upper of str object at 0x0000001244235FB8>
None
>>> s='Hello'
>>> for c in s:
	if c.islower():
		print c
		
SyntaxError: Missing parentheses in call to 'print'
>>> for c in s:
	if c.islower():
		print (c)

		
e
l
l
o
>>> def conv(x):
	l=[]
	for c in x.strip():
		if c.islower():
			l.append(c.upper())
		elif c.isupper():
			l.append(c.lower())
	print(str(l).strip('[]'))

>>> conv('Hello')
'h', 'E', 'L', 'L', 'O'
>>> def conv(x):
	l=[]
	for c in x.strip():
		if c.islower():
			l.append(c.upper())
		elif c.isupper():
			l.append(c.lower())
	print(''.join(str(l).strip('[]')))

	
>>> conv('Hello')
'h', 'E', 'L', 'L', 'O'
>>> def conv(x):
	l=[]
	for c in x.strip():
		if c.islower():
			l.append(c.upper())
		elif c.isupper():
			l.append(c.lower())
	print(''.join(l))

	
>>> conv('Hello')
hELLO
>>> def conv(x):
	l=[]
	for c in x:
		if c.islower():
			l.append(c.upper())
		elif c.isupper():
			l.append(c.lower())
	print(''.join(l))

	
>>> conv('Hello')
hELLO
>>> 
