Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os, glob
>>> metadata=[(f,os.stat(f)) for f in glob.glob('*test.py')]
>>> metadata[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    metadata[0]
IndexError: list index out of range
>>> metadata=[(f,os.stat(f)) for f in glob.glob('*diff.py')]
>>> metadata
[]
>>> metadata=[(f,os.stat(f)) for f in glob.glob('*python.py')]
>>> metadata
[]
>>> os.cwd
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.cwd
AttributeError: module 'os' has no attribute 'cwd'
>>> os.path.cwd
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    os.path.cwd
AttributeError: module 'ntpath' has no attribute 'cwd'
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Users\\maslah\\AppData\\Local\\Programs\\Python\\Python35'
>>> os.c
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.c
AttributeError: module 'os' has no attribute 'c'
>>> os.chdir ('C:\Users\maslah\AppData\Local\Programs\Python\Python35\Tools\scripts')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir ('/Users/maslah/AppData/Local/Programs/Python/Python35/Tools/scripts')
>>> metadata=[(f,os.stat(f)) for f in glob.glob('*find.py')]
>>> metadata
[]
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Users\\maslah\\AppData\\Local\\Programs\\Python\\Python35\\Tools\\scripts'
>>> metadata=[(f,os.stat(f)) for f in glob.glob('*find*.py')]
>>> metadata
[('find-uname.py', os.stat_result(st_mode=33206, st_ino=844424930274105, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=1247, st_atime=1463763221, st_mtime=1442949104, st_ctime=1442949104)), ('finddiv.py', os.stat_result(st_mode=33206, st_ino=844424930274106, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=2586, st_atime=1463763222, st_mtime=1442949104, st_ctime=1442949104)), ('findlinksto.py', os.stat_result(st_mode=33206, st_ino=844424930274107, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=1114, st_atime=1463763222, st_mtime=1442949104, st_ctime=1442949104)), ('findnocoding.py', os.stat_result(st_mode=33206, st_ino=844424930274108, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=3058, st_atime=1463763222, st_mtime=1442949104, st_ctime=1442949104)), ('find_recursionlimit.py', os.stat_result(st_mode=33206, st_ino=844424930274104, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=4123, st_atime=1463763221, st_mtime=1442949104, st_ctime=1442949104))]
>>> metadata[0]
('find-uname.py', os.stat_result(st_mode=33206, st_ino=844424930274105, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=1247, st_atime=1463763221, st_mtime=1442949104, st_ctime=1442949104))
>>> meta_dict={f:os.stat(f) for f in glob.glob('*find*.py')]
SyntaxError: invalid syntax
>>> meta_dict={f:os.stat(f) for f in glob.glob('*find*.py')}
>>> meta_dict
{'findnocoding.py': os.stat_result(st_mode=33206, st_ino=844424930274108, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=3058, st_atime=1463763222, st_mtime=1442949104, st_ctime=1442949104), 'finddiv.py': os.stat_result(st_mode=33206, st_ino=844424930274106, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=2586, st_atime=1463763222, st_mtime=1442949104, st_ctime=1442949104), 'findlinksto.py': os.stat_result(st_mode=33206, st_ino=844424930274107, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=1114, st_atime=1463763222, st_mtime=1442949104, st_ctime=1442949104), 'find-uname.py': os.stat_result(st_mode=33206, st_ino=844424930274105, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=1247, st_atime=1463763221, st_mtime=1442949104, st_ctime=1442949104), 'find_recursionlimit.py': os.stat_result(st_mode=33206, st_ino=844424930274104, st_dev=1660002500, st_nlink=1, st_uid=0, st_gid=0, st_size=4123, st_atime=1463763221, st_mtime=1442949104, st_ctime=1442949104)}
>>> meta_dict .keys
<built-in method keys of dict object at 0x0000000883646BC8>
>>> meta_dict .keys()
dict_keys(['findnocoding.py', 'finddiv.py', 'findlinksto.py', 'find-uname.py', 'find_recursionlimit.py'])
>>> print(os.path.join ('/Users/maslah/documents/python','*find*.py')
      )
/Users/maslah/documents/python\*find*.py
>>> print(os.path.join ('/Users/maslah/documents/python/','*find*.py')
      )
/Users/maslah/documents/python/*find*.py
>>> #check the diff btn the two
>>> print (os.path.expanduser ())
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print (os.path.expanduser ())
TypeError: expanduser() missing 1 required positional argument: 'path'
>>> print (os.path.expanduser ('~'))
C:\Users\maslah
>>> pathname= '/Users/maslah/documents/python/test.py'
>>> os.path.split(pathname)
('/Users/maslah/documents/python', 'test.py')
>>> (dirname,filename)=os.path.split(pathname)
>>> dirname
'/Users/maslah/documents/python'
>>> filename
'test.py'
>>> (shortname,extension)=os.path.splitext (filename)
>>> shortname
'test'
>>> extension
'.py'
>>> print (os.getcwd())
C:\Users\maslah\AppData\Local\Programs\Python\Python35\Tools\scripts
>>> os.chdir(pathname)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    os.chdir(pathname)
FileNotFoundError: [WinError 2] The system cannot find the file specified: '/Users/maslah/documents/python/test.py'
>>> os.chdir('/Users/maslah/Documents/Python')
>>> meta=os.stat('practice.py')
>>> meta.st_mtime
1463831316.9058063
>>> meta.st_atime
1463831316.900808
>>> import time
>>> time.localtime (meta.st_atime )
time.struct_time(tm_year=2016, tm_mon=5, tm_mday=21, tm_hour=14, tm_min=48, tm_sec=36, tm_wday=5, tm_yday=142, tm_isdst=0)
>>> meta.st_size
6851
>>> import humansize
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    import humansize
ImportError: No module named 'humansize'
>>> import first
>>> first.approximate_size (meta.st_size )
'6.7 KiB'
>>> print (os.path.realpath ('first.py')
       )
C:\Users\maslah\Documents\Python\first.py
>>> 
