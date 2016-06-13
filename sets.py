Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> aset={1,2}
>>> aset
{1, 2}
>>> aset.add(4)
>>> aset.add(5,6)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    aset.add(5,6)
TypeError: add() takes exactly one argument (2 given)
>>> aset.update({3,4,6}
	    )
>>> aset
{1, 2, 3, 4, 6}
>>> aset.update({5,2,4},{7,1,9,13})
>>> aset
{1, 2, 3, 4, 5, 6, 7, 9, 13}
>>> aset.update([10,20,30])
>>> aset
{1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 20, 30}
>>> bset={1,3,5,7}
>>> aset.clear ()
>>> aset
set()
>>> aset={1,2,3,4,5,6,7,8,9}
>>> aset.issuperset(bset)
True
>>> aset.issubset(bset)
False
>>> bset.issubset(ase)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    bset.issubset(ase)
NameError: name 'ase' is not defined
>>> bset.issubset(aset)
True
>>> aset.remove(3)
>>> aset.remove(5)
>>> aset.remove(8)
>>> aset
{1, 2, 4, 6, 7, 9}
>>> bset
{1, 3, 5, 7}
>>> aset.union(bset)
{1, 2, 3, 4, 5, 6, 7, 9}
>>> aset.intersection (bset)
{1, 7}
>>> aset.difference(bset)
{9, 2, 4, 6}
>>> aset.symmetric_difference(bset)
{2, 3, 4, 5, 6, 9}
>>> aset.symmetric_difference_update
<built-in method symmetric_difference_update of set object at 0x000000A89AA012E8>
>>> aset.symmetric_difference_update(bset)
>>> aset
{2, 3, 4, 5, 6, 9}
>>> bset
{1, 3, 5, 7}
>>> aset.symmetric_difference(bset)==bset.symmetric_difference (aset)
True
>>> 
