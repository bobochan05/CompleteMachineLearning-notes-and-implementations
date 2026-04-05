'''text method for string data 
here are some common text methods for string data in pandas:
1. str.lower(): Convert strings to lowercase.
2. str.upper(): Convert strings to uppercase.
3. str.split(','): Split strings into lists.
4. str.join(): Join lists into strings.
5. str.split(',', expand=True): Split strings into separate columns.
6. str.cat(): Concatenate strings from a Series or list.'''

import pandas as pd 
name = pd.Series(['andrew','bobo','claire','david','4'])
print(name.str.capitalize())

t = ['GOOG,APPL,AMZN','JPM,BAC,GS']
t1=pd.Series(t)
print(t1)
print(t1.str.split(','))
print(t1.str.split(',', expand=True))
print(t1.str.cat(sep=','))

messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
print(messy_names)
print(messy_names.str.replace(";",""))
print(messy_names.str.replace(";","").str.strip())


