Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mylist = [2,3,4,5]
>>> val *2 for val in mylist
SyntaxError: invalid syntax
>>> return val * 2 for val in mylist
SyntaxError: invalid syntax
>>> elem *2 for val in mylist
SyntaxError: invalid syntax
>>> [val *2 for val in mylist]
[4, 6, 8, 10]
>>> [val **2 for val in mylist]
[4, 9, 16, 25]
>>> def iseven():
	nums=[1,2,3,4,6,7,8]
	[(val,True) for val in nums if  val%2==0 else (val, False)]
	
SyntaxError: invalid syntax
>>> nums=[1,2,3,4,6,7,8]
>>> [True for val in nums if  val%2==0 else False]
SyntaxError: invalid syntax
>>> nums=[1,2,3,4,6,7,8
      [True for val in nums if  val%2==0 else False]
      
SyntaxError: invalid syntax
>>> nums=[1,2,3,4,6,7,8
      [True for val in nums if  val%2==0 ]
      
SyntaxError: invalid syntax
>>> ['True' for val in nums if  val%2==0 else 'False']
SyntaxError: invalid syntax
>>> [val for val in nums if  val%2==0 ]
[2, 4, 6, 8]
>>> [(val, True) for val in nums if  val%2==0 ]
[(2, True), (4, True), (6, True), (8, True)]
>>> [val for val in nums if  val%2==0 else val+1]
SyntaxError: invalid syntax
>>> chars = 'abcde'
>>> ascii
<built-in function ascii>
>>> ascii(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ascii(a)
NameError: name 'a' is not defined
>>> ascii('a')
"'a'"
>>> chars =[72,94,81,56]
>>> [chr(x) for x in chars]
['H', '^', 'Q', '8']
>>> def isprime(k):
	if k=1:
		
SyntaxError: invalid syntax
>>> def isprime(k):
	if k==1:
		return False
	else:
		for i in range(2,k+1):
			if k%i==0:
				return False
		else:
			return True

	
>>> isprime(9)
False
>>> isprime(3)
False
>>> isprime(1)
False
>>> def isprime(k):
	if k==1:
		return False
	else:
		for i in range(2,k):
			if k%i==0:
				return False
		else:
			return True

		
>>> isprime(3)
True
>>> isprime(9)
False
>>> isprime(5)
True
>>> isprime(0)
True
>>> [isprime(z) for z in nums]
[False, True, True, False, False, True, False]
>>> [(z,isprime(z)) for z in nums]
[(1, False), (2, True), (3, True), (4, False), (6, False), (7, True), (8, False)]
>>> slice[(z,isprime(z)) for z in nums]
SyntaxError: invalid syntax
>>> slice[(z,isprime(z)) for z in nums]
SyntaxError: invalid syntax
>>> def fact(x):
	[x *x-1 for x in range(4)]

	
>>> def fact(x):
	[x *x-1 for x in range(x)]

	
>>> fact(4)
>>> [x *x-1 for x in range(4)]
[-1, 0, 3, 8]
>>> [x *x-1 for x in range(2,4)]
[3, 8]
>>> def fact(x):
	[x *fact(x-1) for x in range(2,x+1)]

	
>>> fact(4)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    fact(4)
  File "<pyshell#58>", line 2, in fact
    [x *fact(x-1) for x in range(2,x+1)]
  File "<pyshell#58>", line 2, in <listcomp>
    [x *fact(x-1) for x in range(2,x+1)]
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> def fact(x):
	[x *=fact(x-1) for x in range(2,x+1)]
	return x
SyntaxError: invalid syntax
>>> adict ={'fname':'Anne', 'mname':'bimax', 'lname':'maslah'}
>>> (keys,vals)=adict
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    (keys,vals)=adict
ValueError: too many values to unpack (expected 2)
>>> keys=adict[0]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    keys=adict[0]
KeyError: 0
>>> keys =adict.keys()
>>> keys
dict_keys(['fname', 'lname', 'mname'])
>>> {val,keys for keys, vals in adict}
SyntaxError: invalid syntax
>>> {val,keys for keys, vals in adict.items()}
SyntaxError: invalid syntax
>>> {val:keys for keys, vals in adict.items}
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    {val:keys for keys, vals in adict.items}
TypeError: 'builtin_function_or_method' object is not iterable
>>> {val:keys for keys, vals in adict.items()}
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    {val:keys for keys, vals in adict.items()}
  File "<pyshell#70>", line 1, in <dictcomp>
    {val:keys for keys, vals in adict.items()}
NameError: name 'val' is not defined
>>> adict.values
<built-in method values of dict object at 0x0000009E6333A888>
>>> adict.value()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    adict.value()
AttributeError: 'dict' object has no attribute 'value'
>>> adict.values()
dict_values(['Anne', 'maslah', 'bimax'])
>>> {vals:key for adict.keys,adict.values in adict.items()}
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    {vals:key for adict.keys,adict.values in adict.items()}
  File "<pyshell#74>", line 1, in <dictcomp>
    {vals:key for adict.keys,adict.values in adict.items()}
AttributeError: 'dict' object attribute 'keys' is read-only
>>> {vals:key for adict.keys(),adict.values() in adict.items()}
SyntaxError: can't assign to function call
>>> vals=adict.values ()
>>> {vals:keys for keys,vals in adict.items()}
{'maslah': 'lname', 'Anne': 'fname', 'bimax': 'mname'}
>>> adict.values
<built-in method values of dict object at 0x0000009E6333A888>
>>> adict.keys()
dict_keys(['fname', 'lname', 'mname'])
>>> newdict={vals:keys for keys,vals in adict.items()}
>>> newdict.keys
<built-in method keys of dict object at 0x0000009E635BB2C8>
>>> newdict.keys()
dict_keys(['maslah', 'Anne', 'bimax'])
>>> 
