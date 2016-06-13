Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> size=10
>>> True+True
2
>>> True+True+True
3
>>> type(1)
<class 'int'>
>>> type("Andela")
<class 'str'>
>>> print type("Andela")
SyntaxError: invalid syntax
>>> print(type("Andela"))
<class 'str'>
>>> type(2.4)
<class 'float'>
>>> type(2/4)
<class 'float'>
>>> isInstanceOf(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    isInstanceOf(1)
NameError: name 'isInstanceOf' is not defined
>>> isinstance(1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    isinstance(1)
TypeError: isinstance expected 2 arguments, got 1
>>> isinstance(1,int)
True
>>> 5+4.3
9.3
>>> 4.0+2
6.0
>>> x=2.56774865
>>> x
2.56774865
>>> int(x)
2
>>> import math
>>> math.floor(x)
2
>>> math.abs(x)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    math.abs(x)
AttributeError: module 'math' has no attribute 'abs'
>>> ab
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ab
NameError: name 'ab' is not defined
>>> abs(x)
2.56774865
>>> 67.8996445224567894521
67.8996445224568
>>> type('d')
<class 'str'>
>>> sys.maxint
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sys.maxint
NameError: name 'sys' is not defined
>>> import sys
>>> sys.maxint
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sys.maxint
AttributeError: module 'sys' has no attribute 'maxint'
>>> sys.m
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sys.m
AttributeError: module 'sys' has no attribute 'm'
>>> sys.maxsize
9223372036854775807
>>> 2**32-1
4294967295
>>> 2**32
4294967296
>>> 4/2
2.0
>>> 11/3
3.6666666666666665
>>> 11//3
3
>>> -11/3
-3.6666666666666665
>>> -11//3
-4
>>> -10//3
-4
>>> import fractions
>>> x=fractions.
SyntaxError: invalid syntax
>>> x=fractions.Fraction (6,4)\

   
>>> x=fractions.Fraction (6,4)
>>> x
Fraction(3, 2)
>>> x*2
Fraction(3, 1)
>>> math.sin(90)
0.8939966636005579
>>> math.sin
<built-in function sin>
>>> math.sin(60)
-0.3048106211022167
>>> math.sin(0)
0.0
>>> math.tan(90)
-1.995200412208242
>>> math.tan(60)
0.320040389379563
>>> math.cos(90)
-0.4480736161291701
>>> def is_it_true(num):
	if num:
		print("num not zero")
	else:
		print("num is zero)
		      
SyntaxError: EOL while scanning string literal
>>> def is_it_true(num):
	if num:
		print("num not zero")
	else:
		print("num is zero")
is_it_true(9)
SyntaxError: invalid syntax
>>> is_it_true(9)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    is_it_true(9)
NameError: name 'is_it_true' is not defined
>>> def is_it_true(num):
	if num:
		print("num not zero")
	else:
		print("num is zero")
    is_it_true(1)
    
SyntaxError: unindent does not match any outer indentation level
>>> def is_it_true(num):
	if num:
		print("num not zero")
	else:
		print("num is zero")

		
>>> is_it_true(1)
num not zero
>>> is_it_true(9)
num not zero
>>> is_it_true(0)
num is zero
>>> my_list=[2,3,4,5]
>>> for x in my_list
SyntaxError: invalid syntax
>>> for x in my_list
SyntaxError: invalid syntax
>>> for x in my_list:
	x*2

	
4
6
8
10
>>> my_list[0]
2
>>> my_list .reverse
<built-in method reverse of list object at 0x000000990A910988>
>>> my_list
[2, 3, 4, 5]
>>> my_list .reverse
<built-in method reverse of list object at 0x000000990A910988>
>>> my_list [-2]
4
>>> len(my_list )
4
>>> my_list [1:3]
[3, 4]
>>> my_list [0:2:1]
[2, 3]
>>> my_list [0,-1]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    my_list [0,-1]
TypeError: list indices must be integers or slices, not tuple
>>> my_list [0:-1]
[2, 3, 4]
>>> my_list = my_list + ['a','b']
>>> my_list
[2, 3, 4, 5, 'a', 'b']
>>> my_list .append (True)
>>> my_list
[2, 3, 4, 5, 'a', 'b', True]
>>> my_list .extend (["Lets see this", 14, 'bingo']
		 )
>>> my_list
[2, 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo']
>>> my_list .insert(1,'maslah')
>>> my_list
[2, 'maslah', 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo']
>>> my_list .count(2)
1
>>> my_list .append(2)
>>> my_list .count (2)
2
>>> 'b' is in my_list
SyntaxError: invalid syntax
>>> 'b' in my_list
True
>>> 'g' in my_list
False
>>> my_list .index (2)
0
>>> my_list .index ('bingo')
10
>>> my_list .tuple ()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    my_list .tuple ()
AttributeError: 'list' object has no attribute 'tuple'
>>> tuple(my_list )
(2, 'maslah', 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo', 2)
>>> my_list .append ('b')
>>> my_list
[2, 'maslah', 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo', 2, 'b']
>>> my_list = tuple (my_list )
>>> my_list .append(9)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    my_list .append(9)
AttributeError: 'tuple' object has no attribute 'append'
>>> list(my_list )
[2, 'maslah', 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo', 2, 'b']
>>> my_list =list(my_list )
>>> my_list
[2, 'maslah', 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo', 2, 'b']
>>> my_list .a
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    my_list .a
AttributeError: 'list' object has no attribute 'a'
>>> my_list .append (9)
>>> my_list
[2, 'maslah', 3, 4, 5, 'a', 'b', True, 'Lets see this', 14, 'bingo', 2, 'b', 9]
>>> del my_list [5]
>>> del my_list [len(my_list )]
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    del my_list [len(my_list )]
IndexError: list assignment index out of range
>>> del my_list [len(my_list )-1]
>>> del my_list [-1]
>>> my_list
[2, 'maslah', 3, 4, 5, 'b', True, 'Lets see this', 14, 'bingo', 2]
>>> type(False)
<class 'bool'>
>>> type(False,)
<class 'bool'>
>>> type((False,))
<class 'tuple'>
>>> type(my_list )
<class 'list'>
>>> my_tuple=tuple(my_list )
>>> my_tuple
(2, 'maslah', 3, 4, 5, 'b', True, 'Lets see this', 14, 'bingo', 2)
>>> sliced=my_tuple
>>> sliced=my_tuple [0:3]
>>> sliced
(2, 'maslah', 3)
>>> (x,y,z)=sliced
>>> x
2
>>> y
'maslah'
>>> z
3
>>> (x,y)=sliced
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    (x,y)=sliced
ValueError: too many values to unpack (expected 2)
>>> (x,y,x,c)=sliced
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    (x,y,x,c)=sliced
ValueError: not enough values to unpack (expected 4, got 3)
>>> 
