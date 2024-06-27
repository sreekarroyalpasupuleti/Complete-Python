import keyword
print(keyword.kwlist) # List all Python Keywords

##output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class','continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global','if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return','try', 'while', 'with', 'yield']


print(len(keyword.kwlist)) #len()--we can find the number values by using this function
#output:35

a = keyword.kwlist
print(type(a))
#output:<class 'list'>