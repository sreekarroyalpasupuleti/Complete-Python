# Keywords are the reserved words in Python and can't be used as an identifier.
# There are total 35 keywords are available in python
# All keywords in Python contain only alphabets.
# These are in lowercase except 3 keywords, True, False & None

# Print the list of all Python keywords
import keyword
print(keyword.kwlist) # List all Python Keywords
# output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class','continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global','if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return','try', 'while', 'with', 'yield']


# Print the total number of keywords in Python
print(len(keyword.kwlist)) # len() --we can find the number values by using this function
# output:35

# Assign keyword list to variable 'a' and print its type

a = keyword.kwlist
print(type(a))
# output:<class 'list'>