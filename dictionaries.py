Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> adict={'fname':'anne','lname':'maslah','age':23}
>>> adict
{'lname': 'maslah', 'age': 23, 'fname': 'anne'}
>>> type(adict)
<class 'dict'>
>>> adict['age']=22
>>> adict
{'lname': 'maslah', 'age': 22, 'fname': 'anne'}
>>> adict['mname':'bimax']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    adict['mname':'bimax']
TypeError: unhashable type: 'slice'
>>> adict['mname']='bimax'
>>> adict
{'mname': 'bimax', 'lname': 'maslah', 'age': 22, 'fname': 'anne'}
>>> SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
      1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
>>> len(SUFFIXES )
2
>>> SUFFIXES [1000]
['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
>>> SUFFIXES [1024]
['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
>>> SUFFIXES [1000][3]
'TB'
>>> 1000 in SUFFIXES
True
>>> details={'name':['anne','bimax','maslah'],'age':22}
>>> details
{'name': ['anne', 'bimax', 'maslah'], 'age': 22}
>>> len(details)
2
>>> details['name']
['anne', 'bimax', 'maslah']
>>> details['name'][1]
'bimax'
>>> type(none)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type(none)
NameError: name 'none' is not defined
>>> type(None)
<class 'NoneType'>
>>> None==''
False
>>> ''==not None
SyntaxError: invalid syntax
>>> ''==(not None)
False
>>> "jg"==(not None)
False
>>> 
